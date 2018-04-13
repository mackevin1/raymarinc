$(document).ready(function(){
    // Counterup plugin
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });
    
    //Owl carousal script
    
    $(".owl-carousel").owlCarousel({
        items:1,
        singleItem:true,
        loop:true,
        navigation:true,
        navigationText: [
          "<div class='control-btn-wrap'><i class='ion-ios-arrow-left'></i></div>",
          "<div class='control-btn-wrap'><i class='ion-ios-arrow-right'></i></div>"
          ],
    });
    
    /// Magnified popup video plugin installation
    $('.show-video').magnificPopup({
      type: 'iframe',

      iframe: {
         markup: '<div class="mfp-iframe-scaler">'+
                    '<div class="mfp-close"></div>'+
                    '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>'+
                    '<div class="mfp-title">Some caption</div>'+
                  '</div>'
      },
      callbacks: {
        markupParse: function(template, values, item) {
         values.title = item.el.attr('title');
        }
      }


    });
    
    /// smooth mouse scroll
    
    // detect if ios or not
    function iOS() {
        var iDevices = [
            'iPad Simulator',
            'iPhone Simulator',
            'iPod Simulator',
            'iPad',
            'iPhone',
            'iPod'
        ];

        if (!!navigator.platform) {
            while (iDevices.length) {
                if (navigator.platform === iDevices.pop()){ return true; }
            }
        }

        return false;
    }
    // detect if mac or not
    function isMac() {
        return navigator.platform.indexOf('Mac') > -1
    }

    (function(){
        if(iOS() || isMac()) {

        } else {
            if (window.addEventListener) window.addEventListener('DOMMouseScroll', wheel, false);
            window.onmousewheel = document.onmousewheel = wheel;
        }
    })();

    function wheel(event) {
        var delta = 0;
        if (event.wheelDelta) delta = event.wheelDelta / 120;
        else if (event.detail) delta = -event.detail / 3;

        handle(delta);
        if (event.preventDefault) event.preventDefault();
        event.returnValue = false;
    }

    function handle(delta) {
        var time = 1000; // delay time
        var distance = 300; // delta point 
        // Dom where it will apply 
        $('html, body').stop().animate({
            scrollTop: $(window).scrollTop() - (distance * delta)
        }, time );
    }

    /// measuring scrolling height 
    $("#navbar").css({ backgroundColor: 'transparent' });
    $(window).scroll(function(){
        if($(window).scrollTop()>100){
            $('#navbar').addClass('navbar-colored');
            var l=$(".navbar-colored").css("margin-top").replace("px", "");
            if(l==0){
                $(".navbar-colored").css({ backgroundColor: '#000' });
            }
        }
        else{
            $('#navbar').removeClass('navbar-colored');
            $("#navbar").css({ backgroundColor: 'transparent' });
        }
        
        
    });
    
    /* Nab Tabs */
    $(".list-group-item").click(function(){
        $(".list-group-item").removeClass('active');
        $(this).addClass('active');
        var slide = $(this).data('slide');
        $(".tab-pane").removeClass("active");
        $(".tab-pane[data-slide="+slide+"]").addClass("active");
    });
    google.maps.event.addDomListener(window, 'load', init);
        
            function init() {
                // Basic options for a simple Google Map
                // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
                var mapOptions = {
                    // How zoomed in you want the map to start at (always required)
                    zoom: 11,
                    scrollwheel: false,
                    // The latitude and longitude to center the map (always required)
                    center: new google.maps.LatLng(40.6700, -73.9400), // New York

                    // How you would like to style the map. 
                    // This is where you would paste any style found on Snazzy Maps.
                    styles: [
                                {
                                    "featureType": "landscape",
                                    "stylers": [
                                        {
                                            "saturation": -100
                                        },
                                        {
                                            "lightness": 65
                                        },
                                        {
                                            "visibility": "on"
                                        }
                                    ]
                                },
                                {
                                    "featureType": "poi",
                                    "stylers": [
                                        {
                                            "saturation": -100
                                        },
                                        {
                                            "lightness": 51
                                        },
                                        {
                                            "visibility": "simplified"
                                        }
                                    ]
                                },
                                {
                                    "featureType": "road.highway",
                                    "stylers": [
                                        {
                                            "saturation": -100
                                        },
                                        {
                                            "visibility": "simplified"
                                        }
                                    ]
                                },
                                {
                                    "featureType": "road.arterial",
                                    "stylers": [
                                        {
                                            "saturation": -100
                                        },
                                        {
                                            "lightness": 30
                                        },
                                        {
                                            "visibility": "on"
                                        }
                                    ]
                                },
                                {
                                    "featureType": "road.local",
                                    "stylers": [
                                        {
                                            "saturation": -100
                                        },
                                        {
                                            "lightness": 40
                                        },
                                        {
                                            "visibility": "on"
                                        }
                                    ]
                                },
                                {
                                    "featureType": "transit",
                                    "stylers": [
                                        {
                                            "saturation": -100
                                        },
                                        {
                                            "visibility": "simplified"
                                        }
                                    ]
                                },
                                {
                                    "featureType": "administrative.province",
                                    "stylers": [
                                        {
                                            "visibility": "off"
                                        }
                                    ]
                                },
                                {
                                    "featureType": "water",
                                    "elementType": "labels",
                                    "stylers": [
                                        {
                                            "visibility": "on"
                                        },
                                        {
                                            "lightness": -25
                                        },
                                        {
                                            "saturation": -100
                                        }
                                    ]
                                },
                                {
                                    "featureType": "water",
                                    "elementType": "geometry",
                                    "stylers": [
                                        {
                                            "hue": "#ffff00"
                                        },
                                        {
                                            "lightness": -25
                                        },
                                        {
                                            "saturation": -97
                                        }
                                    ]
                                }
                            ]
                };

                // Get the HTML DOM element that will contain your map 
                // We are using a div with id="map" seen below in the <body>
                var mapElement = document.getElementById('map');

                // Create the Google Map using our element and options defined above
                var map = new google.maps.Map(mapElement, mapOptions);

                // Let's also add a marker while we're at it
                var marker = new google.maps.Marker({
                    position: new google.maps.LatLng(40.6700, -73.9400),
                    map: map,
                    title: 'Snazzy!'
                });
            }
    // Navbar toggle on click link
    $('.nav a').on('click', function(){
        $('.navbar-toggle').click() //bootstrap 3.x by Richard
    });
    
        //contact script
    
    $("#contact_form").submit(function(e){

        e.preventDefault();
        var $ = jQuery;

        var postData 		= $(this).serializeArray(),
            formURL 		= $(this).attr("action"),
            $cfResponse 	= $('#response'),
            $cfsubmit 		= $("#submit"),
            cfsubmitText 	= $cfsubmit.text();

        $cfsubmit.text("Sending...");


        $.ajax(
            {
                url : formURL,
                type: "POST",
                data : postData,
                success:function(data)
                {
                    $cfResponse.html(data);
                    $cfsubmit.text(cfsubmitText);
                    $("#contact_form")[0].reset();
                },
                error: function(data)
                {
                    alert("Error occurd! Please try again");
                    $cfsubmit.text(cfsubmitText);
                }
            });

        return false;

    });
	
	$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});

    
});

/// background video

