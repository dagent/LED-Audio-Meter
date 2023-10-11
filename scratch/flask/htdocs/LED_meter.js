
/*
cmeter.js -- helper functions to input data into the meter/level objects

Assumes an appropriate cmeter.css, populating:
  <div class="LEDmeters" id="LEDmeters">
    <div class="LEDmeter" id="LEDmeterL"></div>
    <div class="LEDmeter" id="LEDmeterR"></div>
  </div>
  */

    var moutputL = document.getElementById("LEDmeterL");
    var moutputR = document.getElementById("LEDmeterR");
    function update_LEDmeterL(data) {
      moutputL.style.clipPath="inset(" + (100 - data) +"% 0 0 0)";
    }
    function update_LEDmeterR(data) {
      moutputR.style.clipPath="inset(" + (100 - data) +"% 0 0 0)";
    }

