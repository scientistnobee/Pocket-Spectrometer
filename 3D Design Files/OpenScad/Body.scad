
height_pd1=12;
height_pd=12;
 
$fn = 100; 
 w_m5=26.0;// width of m5stick
 h_m5=45;// height of m5stick
 t_m5=16; // thickness of m5stick
 wall=1.5; //wall of the body
 tol=0.5; //tolerance for printing
 
 difference(){
 union() {

     
      translate([0,0,0]) 
     cube ([h_m5,w_m5+tol+3,w_m5+tol+2], center=true);  //cuvette holder
     
           translate([-5,0,0]) 
     cube ([h_m5,w_m5+tol+3,w_m5+tol+2], center=true);  // extra cuvette holder bottom
     
     
       translate([0,18,0]) 
       cube ([h_m5, t_m5+tol, w_m5+tol+2], center=true);
     
            translate([-5,18,0]) 
       cube ([h_m5, t_m5+tol, w_m5+tol+2], center=true); //extra bottom part
     
     
      

 
     
 }
 union() {
      

         
          translate([21.0,-2.5,0])
     rotate([0,90,0])
     cylinder(d=24, h=4, center=true);// space for cap
     
  translate([-10,-14.8,-7])
rotate([90,0,0])
ams2();   //space for AMS spectral sensor
     
           translate([-24.0,4,8]) 
            cube ([8, 6, 13], center=true);// for wiring4
    
             translate([-14.0,4,13]) 
            cube ([22, 6, 3], center=true);// for wiring3

      
                  translate([-0.5,-14,10]) 
            cube ([6, 6, 3], center=true);// for wiring3c
     
            translate([-0.5,-4,13]) 
            cube ([6, 22, 3], center=true);// for wiring2
     
           translate([-24.0,4,0]) 
            cube ([8, 40, 6], center=true);// for wiring1 bottom
     
     translate([4,-2.5,0]) 
          cube ([h_m5+tol,13.0,13.0], center=true); //cuvette
            color([1,0,0.5])
        translate([0.5,17.5,0]) 
            cube ([ h_m5, t_m5-wall-0.5, w_m5-wall-0.5], center=true);//m5stickc
            
translate([11.0,18,13]) 
cube ([8, 9, 3], center=true);// for m5 buttonB

 
 
 translate([-12,18,-13]) 
cube ([8, 9, 3], center=true);// for m5 buttonC
 
 
  translate([3,18,-13]) 
cube ([h_m5, 1, 3], center=true);// for m5 slit1


translate([3,18,13]) 
cube ([h_m5, 1, 3], center=true);// for m5 slit2
 
               color([0.5,0,0.5])
        translate([-20,18,0]) 
           cube ([20,12,14], center=true); 
     
        translate([3,28,0]) 
           cube([44,10,16], center=true);//oled screen
     
             translate([2,7,0]) 
     cube ([45,3,15], center=true);  //optical_filter
     
     
             translate([5,3,0]) 
           cube([40,8,8], center=true);//optical sensor window 
   
 }
 }


module buttons(){
 translate([-12,19,-13.25]) 
cube ([5, 8, 2], center=true);// button for m5 buttonC
 
 
 translate([11.0,16.5,13.15]) 
cube ([5, 9, 2.2], center=true);// for m5 buttonB
}

module ams1(){

union(){
    translate([0,0,-1])
cube ([22.5,20.5,2.0]);  // PCB


color([0.4,0.6,0.1])
translate([3.4,3,-2.0])
union(){
translate([0,0,0])
cylinder(d=2.9, h=10);//screw hole1

translate([15.1,0,0])
cylinder(d=2.9, h=10);//screw hole2
}
}
union(){


color([0.4,0.6,0.5])

translate([0,8.5,-2.5])
union(){
    
    translate([10-0.1,0,0])
cube ([2.2,3.5,4]); //Ams sensor
translate([6.1,0,0])    
cube ([1.5,3.5,4]); //LED1
    translate([14.1,0,0])    
cube ([1.5,3.5,4]); //LED2
    
}
}


}

module ams2(){

union(){
       translate([-1,0,-2])
cube ([22,16,5.0]);  // PCB

       translate([-1.0,12,-4.5])
cube ([18.5,4,3.0]);  // PCB holes 


}
union(){

    
color([0.4,0.6,0.1])
translate([2,2,-4.0])
union(){
translate([0,0,-2])
cylinder(d=3, h=10);//screw hole1

translate([14,0,-2])
cylinder(d=3, h=10);//screw hole2
}
color([0.4,0.6,0.5])

translate([0,5.5,-4.5])
union(){
    
    translate([8-0.1,0,-2])
cube ([2.3,4.5,10]); //Ams sensor
translate([4.3,0,-2])    
cube ([2.2,4.5,10]); //LED1
    translate([12.3,0,-2])    
cube ([2.2,4.5,10]); //LED2
    
}
}
}






 module cap(){
difference(){
 union() {
 rotate([0,90,0])
         translate([0,0,0])
     cylinder(d=23.5, h=12, center=true);
     
 }

 union() {
              translate([-0.1,0.0,0.0])
 rotate([0,90,0])

     cylinder(d=20, h=12, center=true);
     }
 
 }
 }
 
//translate([30,-3,0])
//cap();
 
  //translate([-10,-12,-7])
//rotate([90,0,0])
//ams2();
 
 buttons();

     
