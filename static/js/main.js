$(document).ready(function(){
  
	main_pic_width=$("#head_img").width();
	$("#head_img").height(main_pic_width*0.5);

	blog_pic_width=$("#blog_img").width();
	$("#blog_img").height(blog_pic_width*0.5625);

	blog_info_width=$(".blog_list").width();
	$(".blog_list").height(blog_info_width*0.2);

	blog_img_height=$(".blog_img").height();
	$(".blog_img").width(blog_img_height/0.5625);

	




	var breakpoint = 0;

		// Function to set equinav breakpoint
		function equiNavBreakpoint () {
			$('.equinav ul.navbar-nav > li').each(function(){ breakpoint += $(this).innerWidth(); }); //add up all menu items width for breakpoint
		}

		equiNavBreakpoint();

		// Function to apply equinav menu
		function equiNavMenu () {

			$('.equinav ul.navbar-nav > li').removeAttr('style');

			var mq = window.matchMedia('(min-width: 768px)');

			var nav = $('.equinav').innerWidth(); // Navbar Width
			var items = $('.equinav ul.navbar-nav > li').length; // Total number of menu items
			var space = nav - breakpoint; // Empty navbar space
			var spacer = parseInt(space / items); // Number of pixels to spread out to individual menu items. Since decimal places is not good with pixels we have to use parseInt.
			var xspace = nav - (breakpoint + (spacer * items)); // The remaining space after getting the spacer with parseInt
			var xspacer = Math.ceil(xspace / items); // The remaning number of pixels to distribute to menu items

			var num = 0;

			if (mq.matches) {

			  if (nav > breakpoint) {

					$('.equinav').removeClass('equinav-collapse');

					if (breakpoint == 0) equiNavBreakpoint();

					$('.equinav ul.navbar-nav > li').each(function(){

							$(this).css({'width':'auto'});

							var itemwidth = 0;
							itemwidth = (num < xspace) ? ($(this).innerWidth() + spacer) + xspacer : $(this).innerWidth() + spacer;

							$(this).css({'width':itemwidth+'px'});

							num++;

							if ( $(this).find('.dropdown-menu').length != 0 ) {
								if (num == items) $(this).find('.dropdown-menu').addClass('pull-right');
								if ($(this).find('.dropdown-menu').innerWidth() < $(this).innerWidth()) $(this).find('.dropdown-menu').css({'width':$(this).innerWidth()+'px'});
							}
					});

				} else {

					$('.equinav').addClass('equinav-collapse');
					$('.equinav ul.navbar-nav > li > .dropdown-menu').removeAttr('style');

				}

			} else {

				$('.equinav').addClass('equinav-collapse');
				$('.equinav ul.navbar-nav > li > .dropdown-menu').removeAttr('style');

			};
		}

		equiNavMenu();

		$(window).resize(function(){
			equiNavMenu();
		});



});