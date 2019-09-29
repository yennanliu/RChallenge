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