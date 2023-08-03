var sliders = document.querySelectorAll('.slider');
var outputs = document.querySelectorAll('.slidecontainer span[id]');

var updateOutput = function() {
  var sliderValue = this.value;
  var output = this.parentNode.querySelector('span[id]');
  output.innerHTML = sliderValue;
};

for (var i = 0; i < sliders.length; i++) {
  sliders[i].addEventListener("input", updateOutput);
  outputs[i].innerHTML = sliders[i].value;
}


