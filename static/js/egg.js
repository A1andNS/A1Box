function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}
function egg() {
    let ls = ['purple', 'LightSlateGray ', 'dodgerblue', 'LightCoral', 'DeepPink','LightSeaGreen'];
    let version = document.getElementsByClassName('text-version')[0];
    let ver_text = document.getElementsByClassName('text')[1];
    let start = ls.indexOf(version.style.background);
    let result = getRndInteger(0,5);
    if (result !== start){
        version.style.background = ls[result];
        ver_text.style.background = ls[result];
    }
    else {
        egg();
    }
}