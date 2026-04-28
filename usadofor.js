let notas=[8,7,6,9,10];
let soma=0;
for(let i=0; i<notas.length;i++){
    soma+=notas[i];
}
let media=soma/notas.length;
console.log("A media é:",media);
for(let x=1;x<=5;x++){
    console.log("contando:",x);
}
let numero=7;
console.log(`tabuadado ${numero}`);
for(let i=1; i <=10;i++){
    let resultado=numero*i;
    console.log(`${numero}x ${i}=${resultado}`);
}
