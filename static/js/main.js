$(document).ready(function(){
  
	main_pic_width=$("#head_img").width();
	$("#head_img").height(main_pic_width*0.5);

	blog_pic_width=$("#blog_img").width();
	$("#blog_img").height(blog_pic_width*0.5625);



	blog_info_width=$(".blog_list").width();


	if($(document).outerWidth()>450)
	{
		$(".blog_list").height(blog_info_width*0.15);
	}
	else{
		$(".blog_list").height(blog_info_width*0.3);
	}

	blog_img_height=$(".blog_img").height();
	
	if($(document).outerWidth()>450)
	{
		$(".blog_img").width(blog_img_height/0.5625);
	}
	else{
		$(".blog_img").width(blog_img_height/0.75);
	}


	//random tag colors

	var tag_class=["label-default","label-success","label-primary","label-danger","label-info","label-warning"];
	$("#tags h5 a span").each(function(){
		var rand=parseInt(Math.random()*6);
		$(this).addClass(tag_class[rand]);

	});

	$(".tag span").each(function(){
		var rand=parseInt(Math.random()*6);
		$(this).addClass(tag_class[rand]);
		$(".tag span.glyphicon").removeClass(tag_class[rand]);
	});

	//return_top
	 $(window).scroll(function(){  
                if ($(window).scrollTop()>100){  
                    $("#return_top").fadeIn(500);  
                }  
                else  
                {  
                    $("#return_top").fadeOut(500);  
                }  
            });  

	  $("#return_top").click(function(){  
                $('body,html').animate({scrollTop:0},1000);  
                return false;  
            });  
	
	$("#ds-thread #ds-reset .ds-replybox .ds-avatar img").addClass("img-circle");

	//responsive navigation	

	$("#content p img").addClass("img-responsive");

	$("#content img").parent().addClass("center_align");

	$("#content embed").parent().addClass("center_align");

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

$(function () {
    // Line wrap back
    var shLineWrap = function () {
        $('.syntaxhighlighter').each(function () {
            // Fetch
            var $sh = $(this),
                $gutter = $sh.find('td.gutter'),
                $code = $sh.find('td.code')
                ;
            // Cycle through lines
            $gutter.children('.line').each(function (i) {
                // Fetch
                var $gutterLine = $(this),
                    $codeLine = $code.find('.line:nth-child(' + (i + 1) + ')')
                    ;
                //alert($gutterLine);
                // Fetch height
                var height = $codeLine.height() || 0;
                if (!height) {
                    height = 'auto';
                }
                else {
                    height = height += 'px';
                    //alert(height);
                }
                // Copy height over
                $gutterLine.attr('style', 'height: ' + height + ' !important'); // fix by Edi, for JQuery 1.7+ under Firefox 15.0
                console.debug($gutterLine.height(), height, $gutterLine.text(), $codeLine);
            });
        });
    };

    // Line wrap back when syntax highlighter has done it's stuff
    var shLineWrapWhenReady = function () {
        if ($('.syntaxhighlighter').length === 0) {
            setTimeout(shLineWrapWhenReady, 10);
        }
        else {
            shLineWrap();
        }
    };

    // Fire
    shLineWrapWhenReady();
});






});