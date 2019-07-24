/

**/



(function( $ ){


	jQuery(window).bind('scroll', function () {

    if ($(window).scrollTop() > 100) {

        $('#mu-header').addClass('mu-fixed-nav');

	    } else {
	        $('#mu-header').removeClass('mu-fixed-nav');
	    }
	});

		var typed = new Typed('#typed', {
		    stringsElement: '#typed-strings',
		    typeSpeed: 20,
		    backSpeed: 20,
		    startDelay: 1000,
		    loop: true,
		    loopCount: Infinity
		});


		$('.mu-skill-progress-bar').appear(function() {

		 	$('.mu-html5-bar').LineProgressbar({
				percentage: 95,
				triggerOnce: true
			});

			$('.mu-css-bar').LineProgressbar({
				percentage: 90,
				triggerOnce: true
			});

			$('.mu-photoshop-bar').LineProgressbar({
				percentage: 85,
				triggerOnce: true
			});

			$('.mu-wordpress-bar').LineProgressbar({
				percentage: 80,
				triggerOnce: true
			});

			$('.mu-jquery-bar').LineProgressbar({
				percentage: 55,
				triggerOnce: true
			});

		});



	/* ----------------------------------------------------------- */
	/*  4. MENU SMOOTH SCROLLING
	/* ----------------------------------------------------------- */


		var lastId,
		topMenu = $(".mu-menu"),
		topMenuHeight = topMenu.outerHeight()+13,

		menuItems = topMenu.find('a[href^=\\#]'),
		scrollItems = menuItems.map(function(){
		  var item = $($(this).attr("href"));
		  if (item.length) { return item; }
		});

		menuItems.click(function(e){
		  var href = $(this).attr("href"),
		      offsetTop = href === "#" ? 0 : $(href).offset().top-topMenuHeight+22;
		  jQuery('html, body').stop().animate({
		      scrollTop: offsetTop
		  }, 1500);
		  e.preventDefault();
		});

		jQuery(window).scroll(function(){
		   var fromTop = $(this).scrollTop()+topMenuHeight;

		   var cur = scrollItems.map(function(){
		     if ($(this).offset().top < fromTop)
		       return this;
		   });
		   cur = cur[cur.length-1];
		   var id = cur && cur.length ? cur[0].id : "";

		   if (lastId !== id) {
		       lastId = id;

		       menuItems
		         .parent().removeClass("active")
		         .end().filter("[href=\\#"+id+"]").parent().addClass("active");
		   }
		});


	/* ----------------------------------------------------------- */
	/*  5. MOBILE MENU CLOSE
	/* ----------------------------------------------------------- */

		jQuery('.mu-menu').on('click', 'li a', function() {
		  $('.in').collapse('hide');
		});







	/* ----------------------------------------------------------- */
	/*  9. BUTTON SMOOTH SCROLL 
	/* ----------------------------------------------------------- */

		$('.view-my-work-btn').on('click',function (e) {
		    e.preventDefault();
		    var target = this.hash,
		    $target = $(target);
		    $('html, body').stop().animate({
		        'scrollTop': $target.offset().top
		    }, 1000, 'swing', function () {
		        window.location.hash = target;
			});
		});




})( jQuery );
