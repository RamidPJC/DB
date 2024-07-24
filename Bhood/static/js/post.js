    var body = document.getElementById('body');
    var spans = document.getElementsByTagName('span');
    var h2 = document.getElementsByTagName('h2');
    var img = document.getElementsByTagName('img');
    var a = document.getElementsByTagName('a');
    function change_back(el) {
        if (el.innerHTML == "Темная тема") {
            el.innerHTML = "Светлая тема";
            body.style.backgroundColor = "#212121";
            for (var i = 0; i < spans.length; i++) {
                spans[i].style.color = "white";
            }
            for (var i = 0; i < h2.length; i++) {
                h2[i].style.color = 'white';
            }
            for (var i = 0; i < img.length; i++) {
                img[i].style.borderColor = 'blueviolet';
            }
            for (var i = 0; i < a.length; i++) {
                a[i].style.color = 'white';
            }
            document.getElementById('div').style.backgroundColor = "blueviolet";
            el.style.color = 'blueviolet';

        }
        else {
            el.innerHTML = "Темная тема";
            body.style.backgroundColor = "white";
            for (var i = 0; i < spans.length; i++) {
                spans[i].style.color = "black";
            }
            for (var i = 0; i < h2.length; i++) {
                h2[i].style.color = 'black';
            }
            for (var i = 0; i < img.length; i++) {
                img[i].style.borderColor = 'aqua';
            }
            for (var i = 0; i < a.length; i++) {
                a[i].style.color = 'black';
            }
            document.getElementById('div').style.backgroundColor = "aqua";
            el.style.color = 'aqua';
        }
    }