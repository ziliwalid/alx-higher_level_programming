-- lists ratings
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS sr
       ON t.`id` = sr.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
