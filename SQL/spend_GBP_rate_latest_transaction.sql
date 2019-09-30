--------------------------------------
-- # spend_GBP_rate_latest_transaction
--------------------------------------

/*
* Explanation : 
Make 1st CTE exchange_ts : get the all exchange rate with ts, from-to currency, and rate
Make 2nd CTE exchange_ts_lag : create "time intervals" by lagging exchange_rates ts  
                               for getting latest exchange_rates for every transaction 
Make 3rd CTE trans_to_GBP : transform  non-GBP transactions to GBP 
                            based on latest exchange_rates for every transaction  
Make 4rd CTE trans_in_GBP : get  GBP transactions
Make 5rd CTE trans_ : union non-GBP transaction, and GBP transactions in GBP currency
Finally query the CTE trans_ and sum transaction amount in GBP per user 

* Steps : 
all exchange rate with from/to currency and timestamp -> exchange rate lag -> transactions in/non GBP within latest exchange_rates before every transaction -> final result
*/

WITH exchange_ts AS
  (SELECT ts,
          from_currency,
          to_currency,
          rate
   FROM exchange_rates
   WHERE to_currency = 'GBP'),
     exchange_ts_lag AS
  (SELECT *,
          lag(ts, -1, NULL) OVER (PARTITION BY from_currency,
                                               to_currency
                                  ORDER BY ts) AS ts_lag
   FROM exchange_rates
   WHERE to_currency = 'GBP' ),
     trans_to_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          t.currency AS currency,
          t.amount*e.rate AS amount_GBP
   FROM transactions t
   INNER JOIN exchange_ts_lag e ON e.from_currency = t.currency
   AND (t.ts >= e.ts
        AND (e.ts_lag > t.ts
             OR e.ts_lag IS NULL))),
     trans_in_GBP AS
  (SELECT user_id,
          ts,
          currency,
          amount AS amount_gbp
   FROM transactions
   WHERE currency = 'GBP' ),
     trans_ AS
  (SELECT *
   FROM trans_to_GBP
   UNION ALL SELECT *
   FROM trans_in_GBP)
SELECT user_id AS user_id,
       SUM(amount_gbp) AS total_spent_gbp
FROM trans_
GROUP BY user_id
ORDER BY user_id