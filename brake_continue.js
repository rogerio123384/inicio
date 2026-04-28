let carros_estacionados = 0 ;
const limitemaximo = 7 ;
console.log("---iniciando verificação de vagas ---");
for(let vaga = 1 ; vaga <= 10; vaga ++){
    if(vaga === 4 || vaga === 7 || vaga === 3){
        console.log('vaga $ {vaga}: [interditada]-pulando...');
   continue; }
   carros_estacionados++;
}