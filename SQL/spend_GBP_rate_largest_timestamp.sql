WITH largest_exchange_ts AS
  (SELECT from_currency,
          to_currency,
          max(ts) AS ts
   FROM exchange_rates
   WHERE to_currency = 'GBP'
   GROUP BY from_currency,
            to_currency),
     largest_timestamp_exchange AS
  (SELECT e.from_currency AS from_currency,
          e.rate AS rate
   FROM exchange_rates e
   INNER JOIN largest_exchange_ts l ON e.from_currency = l.from_currency
   AND e.to_currency = l.to_currency
   AND e.ts = l.ts),
     trans_to_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          l.from_currency AS currency,
          t.amount*l.rate AS amount_GBP
   FROM transactions t
   INNER JOIN largest_timestamp_exchange l ON l.from_currency = t.currency),
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