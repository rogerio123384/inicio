import pyautogui as pd
import time

texto =  """O aumento da intensidade e da frequência de eventos extremos são apontados como consequências da mudança do clima, que é provocada pela ação humana pela emissão de gases de efeito estufa (GEE). As projeções mais recentes do Painel Intergovernamental sobre Mudança do Clima (IPCC) também apontam enchentes compostas e precipitações intensas causadas por múltiplas condições climáticas, atribuídas à influência humana.

Na avaliação do físico e professor da Universidade de São Paulo (USP), Paulo Artaxo, o trágico episódio de chuvas torrenciais concentradas sobre o Rio Grande do Sul nos últimos dias pode ser considerado a materialização do aumento da frequência e da intensidade de eventos extremos previstos pelo IPCC. "Não há dúvida que esse aumento de enchentes, essas chuvas muito torrenciais, são definitivamente associadas com as mudanças climáticas e a aceleração dessas mudanças no nosso planeta inteiro", afirma o cientista, que é um dos mais expoentes pesquisadores brasileiros sobre o tema. "O aumento da intensidade e da frequência de eventos climáticos extremos está ocorrendo no mundo todo. Não é somente no Rio Grande do Sul. Em São Paulo, com essa onda de calor que já dura duas semanas completamente atípica para o mês de abril e maio. Chuvas torrenciais – têm sido registradas – em vários locais do planeta", complementa Artaxo.

De acordo com recentes estudos de atribuição do World Weather Attribution, que são elaborados por uma rede internacional de cientistas, a mudança do clima foi o principal fator que potencializou a ocorrência de eventos extremos de chuvas. Entre os episódios analisados neste ano estão as ocorrências em Omã e Emirados Árabes Unidos, Filipinas e Irlanda. No extremo oposto, a mudança do clima também foi o principal fator da seca histórica na Amazônia em 2023, que atingiu nível excepcional.

[...]

Eventos de precipitação intensa no continente, por exemplo, que entre 1850 e 1900 ocorriam uma vez a cada dez anos, com o aumento de 1°C podem aumentar a ocorrência em 1,3 vezes em uma década e a intensidade em 6,7%. Se o nível de aquecimento atingir 1,5°C, provavelmente podem ocorrer a 1,5 vezes com intensidade 10,5% maior.

De acordo com o Relatório do Estado do Clima Global, publicado em março deste ano pela Organização Meteorológica Mundial (WMO), a temperatura média global em 2023 ficou 1,45°C mais quente, comparada aos níveis pré-industriais, e muito próxima do limite de 1,5°C. No ano passado, o planeta quebrou todos os recordes dos indicadores climáticos, com oceanos mais aquecidos. Os dados apontam para a necessidade de ação imediata, profunda e consistente de redução de emissões de GEE e de implementação de medidas de adaptação à mudança do clima. """

time.sleep(10)

pd.write(texto)
