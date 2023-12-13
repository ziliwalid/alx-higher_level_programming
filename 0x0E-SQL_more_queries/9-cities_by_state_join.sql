-- does some selecting
SELECT c.`id`, c.`name`, st.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS st
       ON c.`state_id` = st.`id`
 ORDER BY c.`id`;
