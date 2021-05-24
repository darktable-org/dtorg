function createSlider (id)
{
    var container = document.getElementById(id),
        img = container.children[1],
        div = container.children[2],
        itg = container.children[3];

    itg.addEventListener('load', function () {
        img.style.clip = 'rect(0px, ' + img.clientWidth*0.5 + 'px ,'+img.clientHeight+'px , 0px)'
        div.style.left = img.clientWidth*0.5+'px';
        });

    container.addEventListener("mousemove", function(e) {
        if(e.buttons == 1)
        {
          img.style.clip = 'rect(0px, ' + e.offsetX+ 'px ,'+img.clientHeight+'px , 0px)'
          div.style.left = e.offsetX+'px';
        }
        return false;
      });
}
