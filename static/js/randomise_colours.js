var col1, col2, col3, col4;

function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex != 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
    col_arr = [`#${colours_array[0]}`, `#${colours_array[1]}`, `#${colours_array[2]}`, `#${colours_array[3]}`]
    return col_arr;
    
  }

colours_array = [
    'CCF1FF', 'E0D7FF', 'FFCCE1', 'D7EEFF', 'FAFFC7', '71E7C2', '23AFD6', 'D5B60D', 'E1CE60', 'FFBOB9',
    'F19195', 'F59138', 'F6CFB8', 'B4DCE1', 'B8DE98', 'EEC151', 'F4AD84', 'BFED26', '8AD1BA', 'CFA0BA',
    'C4C8DB', 'D4DAD3', 'AC90BB', '95D4A3', '96D2CF', 'F9A2BF', 'FADE7D'
]


function change_colours(){
  var col_arr = shuffle(colours_array);
  document.getElementById("boxOne").style.backgroundColor =col_arr[0];
  document.getElementById("boxTwo").style.backgroundColor =col_arr[1];
  document.getElementById("boxThree").style.backgroundColor =col_arr[2];
  document.getElementById("boxFour").style.backgroundColor =col_arr[3];
  // var box2 = document.getElementById("one");    
  // box2.style="color:`#${col_arr[1]}`;";
  // var box3 = document.getElementById("one");    
  // box3.style="color:`#${col_arr[2]}`;";
  // var box4 = document.getElementById("one");    
  // box4.style="color:`#${col_arr[3]}`;";
}



// console.log(col_arr);
