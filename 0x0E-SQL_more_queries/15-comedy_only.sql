-- Lists
SELECT t.`title`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_genres` AS tv
       ON t.`id` = tv.`show_id`

       INNER JOIN `tv_genres` AS g
       ON g.`id` = tv.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY t.`title`;
