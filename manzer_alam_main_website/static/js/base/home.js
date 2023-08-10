var words = ['y Craft', 'y Passion', 'y Hobby'],
    part,
    i = 0,
    offset = 0,
    len = words.length,
    forwards = true,
    skip_count = 0,
    skip_delay = 15,
    speed = 70;

var wordflick = function () {
    setInterval(function () {
      if (forwards) {
        if (offset >= words[i].length) {
          ++skip_count;
          if (skip_count == skip_delay) {
            forwards = false;
            skip_count = 0;
          }
        }
      }
      else {
        if (offset == 0) {
          forwards = true;
          i++;
          offset = 0;
          if (i >= len) {
            i = 0;
          }
        }
      }
      part = words[i].substr(0, offset);
      if (skip_count == 0) {
        if (forwards) {
          offset++;
        }
        else {
          offset--;
        }
      }
      $('.word').text(part);
    },speed);
};


function changeTo(name) {
  var importanceList = document.getElementById("favCaseStudies");
  var nameList = document.getElementById("favCaseStudiesName");
  var viewsList = document.getElementById("favCaseStudiesViews");
  importanceList.classList.add("hidden");
  nameList.classList.add("hidden");
  viewsList.classList.add("hidden");
  switch (name) {
    case "importance":
      importanceList.classList.remove("hidden");
      break;
    case "name":
      nameList.classList.remove("hidden");
      break;
    case "views":
      viewsList.classList.remove("hidden");
      break;
    default:
      break;
  }
  var selected_btns = document.getElementsByClassName('selected')
  for (const b in selected_btns) {
    if (Object.hasOwnProperty.call(selected_btns, b)) {
      const element = selected_btns[b];
      element.classList.remove('selected');
    }
  }
  var btn = document.getElementById(name + '-btn');
  btn.classList.add('selected');
}

$(document).ready(function () {
  wordflick();
  changeTo("importance");
});
