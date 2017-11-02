         $( "#act1" ).click(function() {
         	if (hide1 == 1) {
		  $( "#preguntas1" ).hide(100);
		  $( "#arr1" ).addClass( "rotating" );
		  hide1 = 0;
		}
		else{
			$( "#preguntas1" ).show(100);
			$( "#arr1" ).removeClass( "rotating" );
			hide1 = 1;
		}
		});


         $( "#comp1" ).click(function() {
            if (hide1 == 1) {
          $( "#preguntas1" ).hide(100);
          $( "#arr1" ).addClass( "rotating" );
          hide1 = 0;
        }
        else{
            $( "#preguntas1" ).show(100);
            $( "#arr1" ).removeClass( "rotating" );
            hide1 = 1;
        }
        });
         var hide2 = 0;
         $( "#act2" ).click(function() {
            if (hide2 == 1) {
          $( "#preguntas2" ).hide(100);
          $( "#arr2" ).addClass( "rotating" );
          hide2 = 0;
        }
        else{
            $( "#preguntas2" ).show(100);
            $( "#arr2" ).removeClass( "rotating" );
            hide2 = 1;
        }
        });
         $( "#comp2" ).click(function() {
            if (hide2 == 1) {
          $( "#preguntas2" ).hide(100);
          $( "#arr2" ).addClass( "rotating" );
          hide2 = 0;
        }
        else{
            $( "#preguntas2" ).show(100);
            $( "#arr2" ).removeClass( "rotating" );
            hide2 = 1;
        }
        });

         var hide3 = 0;
         $( "#act3" ).click(function() {
            if (hide3 == 1) {
          $( "#preguntas3" ).hide(100);
          $( "#arr3" ).addClass( "rotating" );
          hide3 = 0;
        }
        else{
            $( "#preguntas3" ).show(100);
            $( "#arr3" ).removeClass( "rotating" );
            hide3 = 1;
        }
        });
         $( "#comp3" ).click(function() {
            if (hide3 == 1) {
          $( "#preguntas3" ).hide(100);
          $( "#arr3" ).addClass( "rotating" );
          hide3 = 0;
        }
        else{
            $( "#preguntas3" ).show(100);
            $( "#arr3" ).removeClass( "rotating" );
            hide3 = 1;
        }
        });

         var hide4 = 0;
         $( "#act4" ).click(function() {
            if (hide4 == 1) {
          $( "#preguntas4" ).hide(100);
          $( "#arr4" ).addClass( "rotating" );
          hide4 = 0;
        }
        else{
            $( "#preguntas4" ).show(100);
            $( "#arr4" ).removeClass( "rotating" );
            hide4 = 1;
        }
        });
         $( "#comp4" ).click(function() {
            if (hide4 == 1) {
          $( "#preguntas4" ).hide(100);
          $( "#arr4" ).addClass( "rotating" );
          hide4 = 0;
        }
        else{
            $( "#preguntas4" ).show(100);
            $( "#arr4" ).removeClass( "rotating" );
            hide4 = 1;
        }
        });


         var hide5 = 0;
         $( "#act5" ).click(function() {
            if (hide5 == 1) {
          $( "#preguntas5" ).hide(100);
          $( "#arr5" ).addClass( "rotating" );
          hide5 = 0;
        }
        else{
            $( "#preguntas5" ).show(100);
            $( "#arr5" ).removeClass( "rotating" );
            hide5 = 1;
        }
        });
         $( "#comp5" ).click(function() {
            if (hide5 == 1) {
          $( "#preguntas5" ).hide(100);
          $( "#arr5" ).addClass( "rotating" );
          hide5 = 0;
        }
        else{
            $( "#preguntas5" ).show(100);
            $( "#arr5" ).removeClass( "rotating" );
            hide5 = 1;
        }
        });


         var hide6 = 0;
         $( "#act6" ).click(function() {
            if (hide6 == 1) {
          $( "#preguntas6" ).hide(100);
          $( "#arr6" ).addClass( "rotating" );
          hide6 = 0;
        }
        else{
            $( "#preguntas6" ).show(100);
            $( "#arr6" ).removeClass( "rotating" );
            hide6 = 1;
        }
        });
         $( "#comp6" ).click(function() {
            if (hide6 == 1) {
          $( "#preguntas6" ).hide(100);
          $( "#arr6" ).addClass( "rotating" );
          hide6 = 0;
        }
        else{
            $( "#preguntas6" ).show(100);
            $( "#arr6" ).removeClass( "rotating" );
            hide6 = 1;
        }
        });


         var hide7 = 0;
         $( "#act7" ).click(function() {
            if (hide7 == 1) {
          $( "#preguntas7" ).hide(100);
          $( "#arr7" ).addClass( "rotating" );
          hide7 = 0;
        }
        else{
            $( "#preguntas7" ).show(100);
            $( "#arr7" ).removeClass( "rotating" );
            hide7 = 1;
        }
        });
         $( "#comp7" ).click(function() {
            if (hide7 == 1) {
          $( "#preguntas7" ).hide(100);
          $( "#arr7" ).addClass( "rotating" );
          hide7 = 0;
        }
        else{
            $( "#preguntas7" ).show(100);
            $( "#arr7" ).removeClass( "rotating" );
            hide7 = 1;
        }
        });


         $( "#centroradar").draggable();
         $( "#cerrar" ).click(function() {
                $( "#centroradar" ).hide(0);
        });
         





         var switch1 = 0
         $( "#p1" ).click(function() {

         	if (switch1 == 1) {
         		$( "#icono1" ).hide(100);
		  $( "#p1" ).removeClass( "botonact" );
		  $( "#p1" ).addClass( "botondes" );
		  switch1 = 0;
		}
		else{
			$( "#icono1" ).show(100);
		  $( "#p1" ).removeClass( "botondes" );
		  $( "#p1" ).addClass( "botonact" );
			switch1 = 1;
		}
		});

          var switch2 = 0
         $( "#p2" ).click(function() {

         	if (switch2 == 1) {
         		$( "#icono2" ).hide(100);
		  $( "#p2" ).removeClass( "botonact" );
		  $( "#p2" ).addClass( "botondes" );
		  switch2 = 0;
		}
		else{
			$( "#icono2" ).show(100);
		  $( "#p2" ).removeClass( "botondes" );
		  $( "#p2" ).addClass( "botonact" );
			switch2 = 1;
		}
		});

         var switch3 = 0
         $( "#p3" ).click(function() {

            if (switch3 == 1) {
                $( "#icono3" ).hide(100);
          $( "#p3" ).removeClass( "botonact" );
          $( "#p3" ).addClass( "botondes" );
          switch3 = 0;
        }
        else{
            $( "#icono3" ).show(100);
          $( "#p3" ).removeClass( "botondes" );
          $( "#p3" ).addClass( "botonact" );
            switch3 = 1;
        }
        });
         var switch4 = 0
         $( "#p4" ).click(function() {

            if (switch4 == 1) {
                $( "#icono4" ).hide(100);
          $( "#p4" ).removeClass( "botonact" );
          $( "#p4" ).addClass( "botondes" );
          switch4 = 0;
        }
        else{
            $( "#icono4" ).show(100);
          $( "#p4" ).removeClass( "botondes" );
          $( "#p4" ).addClass( "botonact" );
            switch4 = 1;
        }
        });

         var switch5 = 0
         $( "#p5" ).click(function() {

            if (switch5 == 1) {
                $( "#icono5" ).hide(100);
          $( "#p5" ).removeClass( "botonact" );
          $( "#p5" ).addClass( "botondes" );
          switch5 = 0;
        }
        else{
            $( "#icono5" ).show(100);
          $( "#p5" ).removeClass( "botondes" );
          $( "#p5" ).addClass( "botonact" );
            switch5 = 1;
        }
        });

         var switch6 = 0
         $( "#p6" ).click(function() {

            if (switch6 == 1) {
                $( "#icono6" ).hide(100);
          $( "#p6" ).removeClass( "botonact" );
          $( "#p6" ).addClass( "botondes" );
          switch6 = 0;
        }
        else{
            $( "#icono6" ).show(100);
          $( "#p6" ).removeClass( "botondes" );
          $( "#p6" ).addClass( "botonact" );
            switch6 = 1;
        }
        });

         var switch7 = 0
         $( "#p7" ).click(function() {

            if (switch7 == 1) {
                $( "#icono7" ).hide(100);
          $( "#p7" ).removeClass( "botonact" );
          $( "#p7" ).addClass( "botondes" );
          switch7 = 0;
        }
        else{
            $( "#icono7" ).show(100);
          $( "#p7" ).removeClass( "botondes" );
          $( "#p7" ).addClass( "botonact" );
            switch7 = 1;
        }
        });

         var switch8 = 0
         $( "#p8" ).click(function() {

            if (switch8 == 1) {
                $( "#icono8" ).hide(100);
          $( "#p8" ).removeClass( "botonact" );
          $( "#p8" ).addClass( "botondes" );
          switch8 = 0;
        }
        else{
            $( "#icono8" ).show(100);
          $( "#p8" ).removeClass( "botondes" );
          $( "#p8" ).addClass( "botonact" );
            switch8 = 1;
        }
        });
         var switch9 = 0
         $( "#p9" ).click(function() {

            if (switch9 == 1) {
                $( "#icono9" ).hide(100);
          $( "#p9" ).removeClass( "botonact" );
          $( "#p9" ).addClass( "botondes" );
          switch9 = 0;
        }
        else{
            $( "#icono9" ).show(100);
          $( "#p9" ).removeClass( "botondes" );
          $( "#p9" ).addClass( "botonact" );
            switch9 = 1;
        }
        });


         var switch10 = 0
         $( "#p10" ).click(function() {

            if (switch10 == 1) {
                $( "#icono10" ).hide(100);
          $( "#p10" ).removeClass( "botonact" );
          $( "#p10" ).addClass( "botondes" );
          switch10 = 0;
        }
        else{
            $( "#icono10" ).show(100);
          $( "#p10" ).removeClass( "botondes" );
          $( "#p10" ).addClass( "botonact" );
            switch10 = 1;
        }
        });


        var switch11 = 0
         $( "#p11" ).click(function() {

            if (switch11 == 1) {
                $( "#icono11" ).hide(100);
          $( "#p11" ).removeClass( "botonact" );
          $( "#p11" ).addClass( "botondes" );
          switch11 = 0;
        }
        else{
            $( "#icono11" ).show(100);
          $( "#p11" ).removeClass( "botondes" );
          $( "#p11" ).addClass( "botonact" );
            switch11 = 1;
        }
        });


         var switch12 = 0
         $( "#p12" ).click(function() {

            if (switch12 == 1) {
                $( "#icono12" ).hide(100);
          $( "#p12" ).removeClass( "botonact" );
          $( "#p12" ).addClass( "botondes" );
          switch12 = 0;
        }
        else{
            $( "#icono12" ).show(100);
          $( "#p12" ).removeClass( "botondes" );
          $( "#p12" ).addClass( "botonact" );
            switch12 = 1;
        }
        });

         var switch13 = 0
         $( "#p13" ).click(function() {

            if (switch13 == 1) {
                $( "#icono13" ).hide(100);
          $( "#p13" ).removeClass( "botonact" );
          $( "#p13" ).addClass( "botondes" );
          switch13 = 0;
        }
        else{
            $( "#icono13" ).show(100);
          $( "#p13" ).removeClass( "botondes" );
          $( "#p13" ).addClass( "botonact" );
            switch13 = 1;
        }
        });


         var switch14 = 0
         $( "#p14" ).click(function() {

            if (switch14 == 1) {
                $( "#icono14" ).hide(100);
          $( "#p14" ).removeClass( "botonact" );
          $( "#p14" ).addClass( "botondes" );
          switch14 = 0;
        }
        else{
            $( "#icono14" ).show(100);
          $( "#p14" ).removeClass( "botondes" );
          $( "#p14" ).addClass( "botonact" );
            switch14 = 1;
        }
        });


         var switch15 = 0
         $( "#p15" ).click(function() {

            if (switch15 == 1) {
                $( "#icono15" ).hide(100);
          $( "#p15" ).removeClass( "botonact" );
          $( "#p15" ).addClass( "botondes" );
          switch15 = 0;
        }
        else{
            $( "#icono15" ).show(100);
          $( "#p15" ).removeClass( "botondes" );
          $( "#p15" ).addClass( "botonact" );
            switch15 = 1;
        }
        });


         var switch16 = 0
         $( "#p16" ).click(function() {

            if (switch16 == 1) {
                $( "#icono16" ).hide(100);
          $( "#p16" ).removeClass( "botonact" );
          $( "#p16" ).addClass( "botondes" );
          switch16 = 0;
        }
        else{
            $( "#icono16" ).show(100);
          $( "#p16" ).removeClass( "botondes" );
          $( "#p16" ).addClass( "botonact" );
            switch16 = 1;
        }
        });


         var switch17 = 0
         $( "#p17" ).click(function() {

            if (switch17 == 1) {
                $( "#icono17" ).hide(100);
          $( "#p17" ).removeClass( "botonact" );
          $( "#p17" ).addClass( "botondes" );
          switch17 = 0;
        }
        else{
            $( "#icono17" ).show(100);
          $( "#p17" ).removeClass( "botondes" );
          $( "#p17" ).addClass( "botonact" );
            switch17 = 1;
        }
        });


         var switch18 = 0
         $( "#p18" ).click(function() {

            if (switch18 == 1) {
                $( "#icono18" ).hide(100);
          $( "#p18" ).removeClass( "botonact" );
          $( "#p18" ).addClass( "botondes" );
          switch18 = 0;
        }
        else{
            $( "#icono18" ).show(100);
          $( "#p18" ).removeClass( "botondes" );
          $( "#p18" ).addClass( "botonact" );
            switch18 = 1;
        }
        });


         var switch19 = 0
         $( "#p19" ).click(function() {

            if (switch19 == 1) {
                $( "#icono19" ).hide(100);
          $( "#p19" ).removeClass( "botonact" );
          $( "#p19" ).addClass( "botondes" );
          switch19 = 0;
        }
        else{
            $( "#icono19" ).show(100);
          $( "#p19" ).removeClass( "botondes" );
          $( "#p19" ).addClass( "botonact" );
            switch19 = 1;
        }
        });


         var switch20 = 0
         $( "#p20" ).click(function() {

            if (switch20 == 1) {
                $( "#icono20" ).hide(100);
          $( "#p20" ).removeClass( "botonact" );
          $( "#p20" ).addClass( "botondes" );
          switch20 = 0;
        }
        else{
            $( "#icono20" ).show(100);
          $( "#p20" ).removeClass( "botondes" );
          $( "#p20" ).addClass( "botonact" );
            switch20 = 1;
        }
        });


         var switch21 = 0
         $( "#p21" ).click(function() {

            if (switch21 == 1) {
                $( "#icono21" ).hide(100);
          $( "#p21" ).removeClass( "botonact" );
          $( "#p21" ).addClass( "botondes" );
          switch21 = 0;
        }
        else{
            $( "#icono21" ).show(100);
          $( "#p21" ).removeClass( "botondes" );
          $( "#p21" ).addClass( "botonact" );
            switch21 = 1;
        }
        });



         var switch22 = 0
         $( "#p22" ).click(function() {

            if (switch22 == 1) {
                $( "#icono22" ).hide(100);
          $( "#p22" ).removeClass( "botonact" );
          $( "#p22" ).addClass( "botondes" );
          switch22 = 0;
        }
        else{
            $( "#icono22" ).show(100);
          $( "#p22" ).removeClass( "botondes" );
          $( "#p22" ).addClass( "botonact" );
            switch22 = 1;
        }
        });



         var switch23 = 0
         $( "#p23" ).click(function() {

            if (switch23 == 1) {
                $( "#icono23" ).hide(100);
          $( "#p23" ).removeClass( "botonact" );
          $( "#p23" ).addClass( "botondes" );
          switch23 = 0;
        }
        else{
            $( "#icono23" ).show(100);
          $( "#p23" ).removeClass( "botondes" );
          $( "#p23" ).addClass( "botonact" );
            switch23 = 1;
        }
        });


         var switch24 = 0
         $( "#p24" ).click(function() {

            if (switch24 == 1) {
                $( "#icono24" ).hide(100);
          $( "#p24" ).removeClass( "botonact" );
          $( "#p24" ).addClass( "botondes" );
          switch24 = 0;
        }
        else{
            $( "#icono24" ).show(100);
          $( "#p24" ).removeClass( "botondes" );
          $( "#p24" ).addClass( "botonact" );
            switch24 = 1;
        }
        });



         var switch25 = 0
         $( "#p25" ).click(function() {

            if (switch25 == 1) {
                $( "#icono25" ).hide(100);
          $( "#p25" ).removeClass( "botonact" );
          $( "#p25" ).addClass( "botondes" );
          switch25 = 0;
        }
        else{
            $( "#icono25" ).show(100);
          $( "#p25" ).removeClass( "botondes" );
          $( "#p25" ).addClass( "botonact" );
            switch25 = 1;
        }
        });



         var switch26 = 0
         $( "#p26" ).click(function() {

            if (switch26 == 1) {
                $( "#icono26" ).hide(100);
          $( "#p26" ).removeClass( "botonact" );
          $( "#p26" ).addClass( "botondes" );
          switch26 = 0;
        }
        else{
            $( "#icono26" ).show(100);
          $( "#p26" ).removeClass( "botondes" );
          $( "#p26" ).addClass( "botonact" );
            switch26 = 1;
        }
        });



         var switch27 = 0
         $( "#p27" ).click(function() {

            if (switch27 == 1) {
                $( "#icono27" ).hide(100);
          $( "#p27" ).removeClass( "botonact" );
          $( "#p27" ).addClass( "botondes" );
          switch27 = 0;
        }
        else{
            $( "#icono27" ).show(100);
          $( "#p27" ).removeClass( "botondes" );
          $( "#p27" ).addClass( "botonact" );
            switch27 = 1;
        }
        });

         var switch28 = 0
         $( "#p28" ).click(function() {

            if (switch28 == 1) {
                $( "#icono28" ).hide(100);
          $( "#p28" ).removeClass( "botonact" );
          $( "#p28" ).addClass( "botondes" );
          switch28 = 0;
        }
        else{
            $( "#icono28" ).show(100);
          $( "#p28" ).removeClass( "botondes" );
          $( "#p28" ).addClass( "botonact" );
            switch28 = 1;
        }
        });



         var switch29 = 0
         $( "#p29" ).click(function() {

            if (switch29 == 1) {
                $( "#icono29" ).hide(100);
          $( "#p29" ).removeClass( "botonact" );
          $( "#p29" ).addClass( "botondes" );
          switch29 = 0;
        }
        else{
            $( "#icono29" ).show(100);
          $( "#p29" ).removeClass( "botondes" );
          $( "#p29" ).addClass( "botonact" );
            switch29 = 1;
        }
        });


         var switch30 = 0
         $( "#p30" ).click(function() {

            if (switch30 == 1) {
                $( "#icono30" ).hide(100);
          $( "#p30" ).removeClass( "botonact" );
          $( "#p30" ).addClass( "botondes" );
          switch30 = 0;
        }
        else{
            $( "#icono30" ).show(100);
          $( "#p30" ).removeClass( "botondes" );
          $( "#p30" ).addClass( "botonact" );
            switch30 = 1;
        }
        });



         var switch31 = 0
         $( "#p31" ).click(function() {

            if (switch31 == 1) {
                $( "#icono31" ).hide(100);
          $( "#p31" ).removeClass( "botonact" );
          $( "#p31" ).addClass( "botondes" );
          switch31 = 0;
        }
        else{
            $( "#icono31" ).show(100);
          $( "#p31" ).removeClass( "botondes" );
          $( "#p31" ).addClass( "botonact" );
            switch31 = 1;
        }
        });


         var switch32 = 0
         $( "#p32" ).click(function() {

            if (switch32 == 1) {
                $( "#icono32" ).hide(100);
          $( "#p32" ).removeClass( "botonact" );
          $( "#p32" ).addClass( "botondes" );
          switch32 = 0;
        }
        else{
            $( "#icono32" ).show(100);
          $( "#p32" ).removeClass( "botondes" );
          $( "#p32" ).addClass( "botonact" );
            switch32 = 1;
        }
        });



         var switch33 = 0
         $( "#p33" ).click(function() {

            if (switch33 == 1) {
                $( "#icono33" ).hide(100);
          $( "#p33" ).removeClass( "botonact" );
          $( "#p33" ).addClass( "botondes" );
          switch33 = 0;
        }
        else{
            $( "#icono33" ).show(100);
          $( "#p33" ).removeClass( "botondes" );
          $( "#p33" ).addClass( "botonact" );
            switch33 = 1;
        }
        });


         var switch34 = 0
         $( "#p34" ).click(function() {

            if (switch34 == 1) {
                $( "#icono34" ).hide(100);
          $( "#p34" ).removeClass( "botonact" );
          $( "#p34" ).addClass( "botondes" );
          switch34 = 0;
        }
        else{
            $( "#icono34" ).show(100);
          $( "#p34" ).removeClass( "botondes" );
          $( "#p34" ).addClass( "botonact" );
            switch34 = 1;
        }
        });


         var switch35 = 0
         $( "#p35" ).click(function() {

            if (switch35 == 1) {
                $( "#icono35" ).hide(100);
          $( "#p35" ).removeClass( "botonact" );
          $( "#p35" ).addClass( "botondes" );
          switch35 = 0;
        }
        else{
            $( "#icono35" ).show(100);
          $( "#p35" ).removeClass( "botondes" );
          $( "#p35" ).addClass( "botonact" );
            switch35 = 1;
        }
        });



         var switch36 = 0
         $( "#p36" ).click(function() {

            if (switch36 == 1) {
                $( "#icono36" ).hide(100);
          $( "#p36" ).removeClass( "botonact" );
          $( "#p36" ).addClass( "botondes" );
          switch36 = 0;
        }
        else{
            $( "#icono36" ).show(100);
          $( "#p36" ).removeClass( "botondes" );
          $( "#p36" ).addClass( "botonact" );
            switch36 = 1;
        }
        });


         var switch37 = 0
         $( "#p37" ).click(function() {

            if (switch37 == 1) {
                $( "#icono37" ).hide(100);
          $( "#p37" ).removeClass( "botonact" );
          $( "#p37" ).addClass( "botondes" );
          switch37 = 0;
        }
        else{
            $( "#icono37" ).show(100);
          $( "#p37" ).removeClass( "botondes" );
          $( "#p37" ).addClass( "botonact" );
            switch37 = 1;
        }
        });



         var switch38 = 0
         $( "#p38" ).click(function() {

            if (switch38 == 1) {
                $( "#icono38" ).hide(100);
          $( "#p38" ).removeClass( "botonact" );
          $( "#p38" ).addClass( "botondes" );
          switch38 = 0;
        }
        else{
            $( "#icono38" ).show(100);
          $( "#p38" ).removeClass( "botondes" );
          $( "#p38" ).addClass( "botonact" );
            switch38 = 1;
        }
        });



         var switch39 = 0
         $( "#p39" ).click(function() {

            if (switch39 == 1) {
                $( "#icono39" ).hide(100);
          $( "#p39" ).removeClass( "botonact" );
          $( "#p39" ).addClass( "botondes" );
          switch39 = 0;
        }
        else{
            $( "#icono39" ).show(100);
          $( "#p39" ).removeClass( "botondes" );
          $( "#p39" ).addClass( "botonact" );
            switch39 = 1;
        }
        });



         var switch40 = 0
         $( "#p40" ).click(function() {

            if (switch40 == 1) {
                $( "#icono40" ).hide(100);
          $( "#p40" ).removeClass( "botonact" );
          $( "#p40" ).addClass( "botondes" );
          switch40 = 0;
        }
        else{
            $( "#icono40" ).show(100);
          $( "#p40" ).removeClass( "botondes" );
          $( "#p40" ).addClass( "botonact" );
            switch40 = 1;
        }
        });


         var switch41 = 0
         $( "#p41" ).click(function() {

            if (switch41 == 1) {
                $( "#icono41" ).hide(100);
          $( "#p41" ).removeClass( "botonact" );
          $( "#p41" ).addClass( "botondes" );
          switch41 = 0;
        }
        else{
            $( "#icono41" ).show(100);
          $( "#p41" ).removeClass( "botondes" );
          $( "#p41" ).addClass( "botonact" );
            switch41 = 1;
        }
        });



         var switch42 = 0
         $( "#p42" ).click(function() {

            if (switch42 == 1) {
                $( "#icono42" ).hide(100);
          $( "#p42" ).removeClass( "botonact" );
          $( "#p42" ).addClass( "botondes" );
          switch42 = 0;
        }
        else{
            $( "#icono42" ).show(100);
          $( "#p42" ).removeClass( "botondes" );
          $( "#p42" ).addClass( "botonact" );
            switch42 = 1;
        }
        });


         var switch43 = 0
         $( "#p43" ).click(function() {

            if (switch43 == 1) {
                $( "#icono43" ).hide(100);
          $( "#p43" ).removeClass( "botonact" );
          $( "#p43" ).addClass( "botondes" );
          switch43 = 0;
        }
        else{
            $( "#icono43" ).show(100);
          $( "#p43" ).removeClass( "botondes" );
          $( "#p43" ).addClass( "botonact" );
            switch43 = 1;
        }
        });


         var switch44 = 0
         $( "#p44" ).click(function() {

            if (switch44 == 1) {
                $( "#icono44" ).hide(100);
          $( "#p44" ).removeClass( "botonact" );
          $( "#p44" ).addClass( "botondes" );
          switch44 = 0;
        }
        else{
            $( "#icono44" ).show(100);
          $( "#p44" ).removeClass( "botondes" );
          $( "#p44" ).addClass( "botonact" );
            switch44 = 1;
        }
        });



         var switch45 = 0
         $( "#p45" ).click(function() {

            if (switch45 == 1) {
                $( "#icono45" ).hide(100);
          $( "#p45" ).removeClass( "botonact" );
          $( "#p45" ).addClass( "botondes" );
          switch45 = 0;
        }
        else{
            $( "#icono45" ).show(100);
          $( "#p45" ).removeClass( "botondes" );
          $( "#p45" ).addClass( "botonact" );
            switch45 = 1;
        }
        });



         var switch46 = 0
         $( "#p46" ).click(function() {

            if (switch46 == 1) {
                $( "#icono46" ).hide(100);
          $( "#p46" ).removeClass( "botonact" );
          $( "#p46" ).addClass( "botondes" );
          switch46 = 0;
        }
        else{
            $( "#icono46" ).show(100);
          $( "#p46" ).removeClass( "botondes" );
          $( "#p46" ).addClass( "botonact" );
            switch46 = 1;
        }
        });


         var switch47 = 0
         $( "#p47" ).click(function() {

            if (switch47 == 1) {
                $( "#icono47" ).hide(100);
          $( "#p47" ).removeClass( "botonact" );
          $( "#p47" ).addClass( "botondes" );
          switch47 = 0;
        }
        else{
            $( "#icono47" ).show(100);
          $( "#p47" ).removeClass( "botondes" );
          $( "#p47" ).addClass( "botonact" );
            switch47 = 1;
        }
        });



         var switch48 = 0
         $( "#p48" ).click(function() {

            if (switch48 == 1) {
                $( "#icono48" ).hide(100);
          $( "#p48" ).removeClass( "botonact" );
          $( "#p48" ).addClass( "botondes" );
          switch48 = 0;
        }
        else{
            $( "#icono48" ).show(100);
          $( "#p48" ).removeClass( "botondes" );
          $( "#p48" ).addClass( "botonact" );
            switch48 = 1;
        }
        });



         var switch49 = 0
         $( "#p49" ).click(function() {

            if (switch49 == 1) {
                $( "#icono49" ).hide(100);
          $( "#p49" ).removeClass( "botonact" );
          $( "#p49" ).addClass( "botondes" );
          switch49 = 0;
        }
        else{
            $( "#icono49" ).show(100);
          $( "#p49" ).removeClass( "botondes" );
          $( "#p49" ).addClass( "botonact" );
            switch49 = 1;
        }
        });


         var switch50 = 0
         $( "#p50" ).click(function() {

            if (switch50 == 1) {
                $( "#icono50" ).hide(100);
          $( "#p50" ).removeClass( "botonact" );
          $( "#p50" ).addClass( "botondes" );
          switch50 = 0;
        }
        else{
            $( "#icono50" ).show(100);
          $( "#p50" ).removeClass( "botondes" );
          $( "#p50" ).addClass( "botonact" );
            switch50 = 1;
        }
        });


         var switch51 = 0
         $( "#p51" ).click(function() {

            if (switch51 == 1) {
                $( "#icono51" ).hide(100);
          $( "#p51" ).removeClass( "botonact" );
          $( "#p51" ).addClass( "botondes" );
          switch51 = 0;
        }
        else{
            $( "#icono51" ).show(100);
          $( "#p51" ).removeClass( "botondes" );
          $( "#p51" ).addClass( "botonact" );
            switch51 = 1;
        }
        });



         var switch52 = 0
         $( "#p52" ).click(function() {

            if (switch52 == 1) {
                $( "#icono52" ).hide(100);
          $( "#p52" ).removeClass( "botonact" );
          $( "#p52" ).addClass( "botondes" );
          switch52 = 0;
        }
        else{
            $( "#icono52" ).show(100);
          $( "#p52" ).removeClass( "botondes" );
          $( "#p52" ).addClass( "botonact" );
            switch52 = 1;
        }
        });



         var switch53 = 0
         $( "#p53" ).click(function() {

            if (switch53 == 1) {
                $( "#icono53" ).hide(100);
          $( "#p53" ).removeClass( "botonact" );
          $( "#p53" ).addClass( "botondes" );
          switch53 = 0;
        }
        else{
            $( "#icono53" ).show(100);
          $( "#p53" ).removeClass( "botondes" );
          $( "#p53" ).addClass( "botonact" );
            switch53 = 1;
        }
        });


         var switch54 = 0
         $( "#p54" ).click(function() {

            if (switch54 == 1) {
                $( "#icono54" ).hide(100);
          $( "#p54" ).removeClass( "botonact" );
          $( "#p54" ).addClass( "botondes" );
          switch54 = 0;
        }
        else{
            $( "#icono54" ).show(100);
          $( "#p54" ).removeClass( "botondes" );
          $( "#p54" ).addClass( "botonact" );
            switch54 = 1;
        }
        });


         var switch55 = 0
         $( "#p55" ).click(function() {

            if (switch55 == 1) {
                $( "#icono55" ).hide(100);
          $( "#p55" ).removeClass( "botonact" );
          $( "#p55" ).addClass( "botondes" );
          switch55 = 0;
        }
        else{
            $( "#icono55" ).show(100);
          $( "#p55" ).removeClass( "botondes" );
          $( "#p55" ).addClass( "botonact" );
            switch55 = 1;
        }
        });



         var switch56 = 0
         $( "#p56" ).click(function() {

            if (switch56 == 1) {
                $( "#icono56" ).hide(100);
          $( "#p56" ).removeClass( "botonact" );
          $( "#p56" ).addClass( "botondes" );
          switch56 = 0;
        }
        else{
            $( "#icono56" ).show(100);
          $( "#p56" ).removeClass( "botondes" );
          $( "#p56" ).addClass( "botonact" );
            switch56 = 1;
        }
        });



         var switch57 = 0
         $( "#p57" ).click(function() {

            if (switch57 == 1) {
                $( "#icono57" ).hide(100);
          $( "#p57" ).removeClass( "botonact" );
          $( "#p57" ).addClass( "botondes" );
          switch57 = 0;
        }
        else{
            $( "#icono57" ).show(100);
          $( "#p57" ).removeClass( "botondes" );
          $( "#p57" ).addClass( "botonact" );
            switch57 = 1;
        }
        });


         var switch58 = 0
         $( "#p58" ).click(function() {

            if (switch58 == 1) {
                $( "#icono58" ).hide(100);
          $( "#p58" ).removeClass( "botonact" );
          $( "#p58" ).addClass( "botondes" );
          switch58 = 0;
        }
        else{
            $( "#icono58" ).show(100);
          $( "#p58" ).removeClass( "botondes" );
          $( "#p58" ).addClass( "botonact" );
            switch58 = 1;
        }
        });



         var switch59 = 0
         $( "#p59" ).click(function() {

            if (switch59 == 1) {
                $( "#icono59" ).hide(100);
          $( "#p59" ).removeClass( "botonact" );
          $( "#p59" ).addClass( "botondes" );
          switch59 = 0;
        }
        else{
            $( "#icono59" ).show(100);
          $( "#p59" ).removeClass( "botondes" );
          $( "#p59" ).addClass( "botonact" );
            switch59 = 1;
        }
        });



         var switch60 = 0
         $( "#p60" ).click(function() {

            if (switch60 == 1) {
                $( "#icono60" ).hide(100);
          $( "#p60" ).removeClass( "botonact" );
          $( "#p60" ).addClass( "botondes" );
          switch60 = 0;
        }
        else{
            $( "#icono60" ).show(100);
          $( "#p60" ).removeClass( "botondes" );
          $( "#p60" ).addClass( "botonact" );
            switch60 = 1;
        }
        });


         var switch61 = 0
         $( "#p61" ).click(function() {

            if (switch61 == 1) {
                $( "#icono61" ).hide(100);
          $( "#p61" ).removeClass( "botonact" );
          $( "#p61" ).addClass( "botondes" );
          switch61 = 0;
        }
        else{
            $( "#icono61" ).show(100);
          $( "#p61" ).removeClass( "botondes" );
          $( "#p61" ).addClass( "botonact" );
            switch61 = 1;
        }
        });


         var switch62 = 0
         $( "#p62" ).click(function() {

            if (switch62 == 1) {
                $( "#icono62" ).hide(100);
          $( "#p62" ).removeClass( "botonact" );
          $( "#p62" ).addClass( "botondes" );
          switch62 = 0;
        }
        else{
            $( "#icono62" ).show(100);
          $( "#p62" ).removeClass( "botondes" );
          $( "#p62" ).addClass( "botonact" );
            switch62 = 1;
        }
        });


         var switch63 = 0
         $( "#p63" ).click(function() {

            if (switch63 == 1) {
                $( "#icono63" ).hide(100);
          $( "#p63" ).removeClass( "botonact" );
          $( "#p63" ).addClass( "botondes" );
          switch63 = 0;
        }
        else{
            $( "#icono63" ).show(100);
          $( "#p63" ).removeClass( "botondes" );
          $( "#p63" ).addClass( "botonact" );
            switch63 = 1;
        }
        });