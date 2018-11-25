<?php
function create_githubrepo_widget() {
         global $wpdb;

         $sql = 'select name, html_url, description from gitrepo';

         $rows = $wpdb->get_results($sql, ARRAY_A);
         $snippet = '<div style="width:305px;margin: 0 auto;">';
         foreach($rows as $row) {
                       $url = $row["html_url"];
                       $name = $row["name"];
                       $snippet .= '<a class="pandanote-info-github" href="'.$url.'"><span style="color:#1E3E8A;font-weight:bold;font-size:130%;">'.$name.'</span></a><br/>'.$row["description"].'<hr/>';
         }
         return $snippet . '</div><div class="clear"></div>';
}

add_shortcode('create-githubrepo-widget','create_githubrepo_widget');
?>
