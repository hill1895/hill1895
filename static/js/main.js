$(document).ready(function(){
  
	main_pic_width=$("#head_img").width();
	$("#head_img").height(main_pic_width*0.5);

	blog_pic_width=$("#blog_img").width();
	$("#blog_img").height(blog_pic_width*0.5625);

	blog_info_width=$(".blog_list").width();
	$(".blog_list").height(blog_info_width*0.2);

	blog_img_height=$(".blog_img").height();
	$(".blog_img").width(blog_img_height/0.5625);



});