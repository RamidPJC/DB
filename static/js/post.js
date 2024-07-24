    var body = document.getElementById('body');
    var spans = document.getElementsByTagName('span');
    var h2 = document.getElementsByTagName('h2');
    var img = document.getElementsByTagName('img');
    var a = document.getElementsByTagName('a');
    function change_back(el) {
        if (el.innerHTML == "Темная тема") {
            el.innerHTML = "Светлая тема";
            body.style.backgroundColor = "#212121";

            document.getElementById('div').style.backgroundColor = "blueviolet";
            el.style.color = 'blueviolet';

        }
        else {
            el.innerHTML = "Темная тема";
            body.style.backgroundColor = "white";

            document.getElementById('div').style.backgroundColor = "aqua";
            el.style.color = 'aqua';
        }
    }