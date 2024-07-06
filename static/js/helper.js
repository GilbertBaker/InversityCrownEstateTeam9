let window_list = []
function $element(name) {
    return document.createElement(name);
}
function $clicked(element,callback) {
    element.onclick = callback;
}
function $insert(parent,...children) {
    for (let index = 0; index < children.length; index++) {
        parent.appendChild(children[index]);
    }
    return children[0];
}
function $html(element,html) {
    element.innerHTML = html;
    return element;
}
function $event(element,name,callback) {
    element.addEventListener(name,callback);
}
function $remove_event(element,name,callback) {
    element.removeEventListener(name,callback)
}
function $get(id) {
    return document.getElementById(id);
}
function $get_class(classname) { // Get all elements of a class (just an alias)
    return document.getElementsByClassName(classname);
}
function $download(path) { // Downloads a file from the server
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", path, false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
        result = xmlhttp.responseText;
    }
    return result;
}