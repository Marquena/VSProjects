function jono(){
    /*tehtävä 3.1*/
    let luvut=[];
    for(let i=0; i<5 ;i++){
        luku=parseInt(prompt("anna luku"));
        luvut.push(luku);
    }
    let html_str="";
    for(let i=luvut.length-1;i>=0;i--){
        luku = luvut[i];
        html_str=string(html_str+luku);
    }
    document.querySelector("#demo").innerHTML = html_str;
}
function nimikeruu(){
    /*tehtävä 3.2 */
    let luku=prompt("monta äijää");
    let jengi = [];
    for(let i=0; i<luku;i++){
        let nimi=prompt("Anna äijän nimi");
        jengi.push(nimi);
    }
    jengi.sort();
    let ab = "<ol>";
    for(let i=0;i<jengi.length;i++){
        ab+="<li>"+jengi[i]+"</li>";
    }
    ab+="</ol>";
    document.querySelector("#demo").innerHTML=ab;
}
function koirat(){
    /*tehtävä 3.3 */
    let dog=[];
    for(i=0;i<6;i++){
        let dq=prompt("anna koiran nimi");
        dog.push(dq);
    }
    dog.sort();
    dog.reverse();
    let ab="<ul>";
    for(let i=0;i<dog.length;i++){
        ab+="<li>"+dog[i]+"</li>";
    }
    ab+="</ul>";
    document.querySelector("#demo").innerHTML=ab;
}

function luvut(){
    /*tehtävä 3.4 */
    let lista=[];
    let kysy = Number(prompt("Anna numero"));
    while(kysy!==0){
        lista.push(kysy);
        kysy = Number(prompt("Anna numero"));
    }
    lista.sort();
    let ab="<ul>";
    for(i=0;i<lista.length;i++){
        ab += "<li>" + lista[i] + "</li>";        
    }
    ab+="</ul>";
    document.querySelector("#demo").innerHTML=ab;
    console.log(lista);
}

const taulukko=["kissa","koira","marsu","pupu"];
let yhd="";
function concat(taulukko){
    /*tehtävä 3.8*/
    for(const eläin of taulukko){
        yhd = yhd+eläin;
    }
    return yhd;
}
function con(){
    /*tehtävä 3.8*/
    document.querySelector("#demo").innerHTML = concat(taulukko);
}

