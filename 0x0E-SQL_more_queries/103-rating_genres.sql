-- does some listing
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS sg
       ON sg.`genre_id` = g.`id`

       INNER JOIN `tv_show_ratings` AS sr
       ON sr.`show_id` = sg.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
