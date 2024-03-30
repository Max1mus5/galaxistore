var crawls = document.getElementsByClassName('crawl');
    var randomIndex = Math.floor(Math.random() * crawls.length);
    var crawlToShow = crawls[randomIndex];

    // Oculta todos los crawls
    for (var i = 0; i < crawls.length; i++) {
        crawls[i].style.display = 'none';
    }

    // Muestra el crawl seleccionado
    crawlToShow.style.display = 'block';

    /* <div class="crawl" id="9" >
                <h1>Episodio IX</h1>
                <p>¡Los muertos hablan! 
                    La galaxia ha escuchado
                    una transmisión misteriosa,
                    una amenaza de VENGANZA
                    en la siniestra voz del fallecido
                    EMPERADOR PALPATINE
                    </p>
                <p>LA GENERAL LEIA ORGANA
                    envía agentes secretos a obtener
                    información, mientras que REY,
                    la última esperanza de los Jedi,
                    entrena para luchar en contra 
                    de la diabólica PRIMERA ORDEN.</p>
                <p>Mientras tanto, el Líder Supremo
                    KYLO REN busca furiosamente
                    al Emperador fantasma,
                    dispuesto a destruir cualquier
                    amenaza a su poder....</p>
        </div>
            <div class="crawl" id="8" >
                <h1>Episodio VIII</h1>
                <p>La PRIMERA ORDEN impera. 
                    Luego de destruir a la pacífica 
                    República, el Líder Supremo Snoke
                    ahora envía a sus despiadadas 
                    legiones a asumir el control
                    militar de la galaxia.
                    </p>
                <p>Sólo la general Leia Organa y 
                    su grupo de combatientes de 
                    la RESISTENCIA se oponen a la 
                    creciente tiranía, convencidos
                    de que el Maestro Jedi
                    Luke Skywalker regresará 
                    y restaurará la chispa de 
                    esperanza en la lucha.</p>
                <p>Pero la Resistencia ha 
                    sido expuesta. Mientras la
                    Primera Orden se dirige 
                    hacia la base rebelde, los 
                    valientes héroes organizan un
                    desesperado escape....</p>
        </div>
            <div class="crawl" id="7" >
                <h1>Episodio VII</h1>
                <p>Luke Skywalker ha desaparecido.
                    En su ausencia, la siniestra
                    PRIMERA ORDEN ha surgido de
                    las cenizas del Imperio y no
                    descansará hasta que Skywalker,
                    el último Jedi, haya sido
                    destruido.
                    </p>
                <p>Con el apoyo de la REPÚBLICA,
                    la General Leia Organa dirige
                    una valiente RESISTENCIA.
                    Desesperadamente busca
                    a su hermano Luke con el fin
                    de obtener su ayuda para
                    restaurar la paz y la justicia
                    en la galaxia.</p>
                <p>Leia ha enviado a su piloto
                    más audaz en una misión secreta
                    a Jakku, donde un viejo aliado
                    ha descubierto una pista
                    del paradero de Luke....</p>
        </div>
            <div class="crawl" id="6" >
                <h1>Episodio VI</h1>
                <p>Luke Skywalker ha regresado 
                    a Tatooine, su planeta de 
                    origen, en un intento de
                    rescatar a su amigo Han 
                    Solo de las garras del vil 
                    Jabba.</p>
                <p>Luke no sabe que el IMPERIO 
                    GALÁCTICO ha iniciado
                    secretamente la construcción
                    de una nueva estación
                    espacial blindada, incluso 
                    más poderosa que la primera 
                    y temida Estrella de la Muerte.</p>
                <p>Una vez terminada, esta arma 
                    extrema augurará una muerte 
                    segura para el pequeño grupo 
                    de rebeldes que lucha por
                    restaurar la libertad en la 
                    galaxia...</p>
        </div>
 <div class="crawl" id="4" >
                <h1>Episodio IV</h1>
                <p>Son tiempos de guerra civil.
                    Naves rebeldes han atacado 
                    desde una base secreta y 
                    han obtenido su primera
                    victoria contra el malvado
                    Imperio Galáctico.</p>
                <p>Durante la batalla, espías
                    rebeldes lograron robar los 
                    planos secretos del arma 
                    más extrema del Imperio,
                    la ESTRELLA DE LA 
                    MUERTE, una estación 
                    espacial blindada con 
                    suficiente potencia para 
                    destruir un planeta entero.
                    </p>
                <p>Perseguida por los 
                    siniestros agentes del 
                    Imperio, la Princesa Leia 
                    se dirige velozmente a casa 
                    en su nave espacial, 
                    mientras resguarda los 
                    planos que pueden salvar 
                    a su pueblo y restaurar la 
                    libertad en la galaxia....</p>
        </div>
            <div class="crawl" id="3" >
                    <h1>Episodio III</h1>
                    <p>¡Guerra! La República se desmorona bajo los ataques del despiadado Conde Dooku, señor de los Sith. Hay héroes en ambos bandos. El mal está por doquier.</p>
                    <p>En una maniobra audaz, el diabólico líder droide, general Grievous, ha entrado a la capital de la República y secuestrado al canciller Palpatine, líder del Senado Galáctico.</p>
                    <p>Mientras el Ejército Droide Separatista trata de huir de la asediada capital con su valioso rehén, dos caballeros Jedi dirigen una misión desesperada para rescatar al canciller cautivo....</p>
            </div>
            <div class="crawl" id="2" >
                <h1>Episodio II</h1>
                <p>Hay inquietud en el Senado
                    Galáctico. Varios miles de
                    sistemas solares han declarado
                    sus intenciones de abandonar 
                    la República.</p>
                <p>El movimiento separatista,
                    bajo el liderazgo del misterioso
                    Conde Dooku, ha hecho difícil
                    que el número limitado de 
                    Caballeros Jedi mantengan la 
                    paz y el orden en la galaxia.</p>
                <p>La Senadora Amidala, la ex
                    reina de Naboo, va a regresar 
                    al Senado Galáctico para 
                    votar sobre la cuestión crítica 
                    de formar un EJÉRCITO DE 
                    LA REPÚBLICA para ayudar a 
                    los abrumados Jedi....</p>
            </div>  
            <div class="crawl" id="1" >
                <h1>Episodio I</h1>
                <p>La República Galáctica está
                    sumida en disturbios. Hay
                    protestas contra la tributación
                    de las rutas comerciales a
                    sistemas estelares.
                    </p>
                <p>Esperando resolver el problema
                    con un bloqueo de mortíferos
                    cruceros, la avariciosa
                    Federación de Comercio ha
                    detenido todos los envíos al
                    pequeño planeta de Naboo.</p>
                <p>Mientras el Congreso de la
                    República debate sin fin
                    esta alarmante cadena de
                    acontecimientos, el Canciller
                    Supremo ha despachado en
                    secreto a dos Caballeros Jedi,
                    los guardianes de la paz y la
                    justicia en la galaxia, a resolver
                    el conflicto....   </p>
            </div> */