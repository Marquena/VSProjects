
function lasku(){
    let luvut = []
    for(let i = 1; i<=3; i++){
        let a = prompt("Anna luku");
        const b = parseInt(a)
        luvut.push(b);
    }
    let plus = luvut[0]+luvut[1]+luvut[2]
    let kert = luvut[0] * luvut[1] * luvut[2];
    let ka = plus/3;

    let printti = "Yhteenlasku: " + plus + "   Tulo: " + kert + "   Keskiarvo: " + ka
    document.getElementById("demo").innerHTML = printti;
}
function potter(){
    let nimi = prompt("Anna nimi");
    let hnum = Math.floor(Math.random(4));
    let house = "a";

    if(hnum==0){
        house = "Gryffindor";
    }
    else if(hnum == 1){
        house = "Slytherin";
    }
    else if(hnum==2){
        house = "Ravenclaw";
    }
    else if(hnum==3){
        house = "Hufflepuff";
    }

    document.getElementById("demo").innerHTML = nimi+", you are a "+house;
}
function hyppy(){
    let vuosi = prompt("Anna vuosi");
    let verdict;
    if(vuosi%400==0){
        verdict = "On hyppyvuosi";
    }
    else if(vuosi%100==0){
        verdict = "Eu ole hyppyvuosi";
    }
    else if(vuosi%4==0){
        verdict = "On hyppyvuosi";
    }
    else{
        verdict = "Ei ole hyppyvuosi";
    }
    document.getElementById("demo").innerHTML = verdict;

}