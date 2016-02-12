Title: Histoire de ce blog
Date: 2016-02-11 18:00
Category: Tech
Author: Sarfraz Houssen Kapasi

Chers lecteurs,

Je me permets de prendre contrôle du blog de ma mére afin de vous parler des changements opérés sur le système servant le blog et pourquoi il y a eu besoin de changer.

<h4>Genèse du blog</h4>

L'idée de la toute première version de ce blog m'est venue suite au constat simple que m'a mère appréciait particulièrement nous aider à faire nos devoirs de français (aucunement une révélation). Mais c'est une constatation qui est arrivée a un moment ou j'essayais de mettre en place la 4eme version de mon blog personnel (ou peut être la 5eme…). J'ai un effet un long passé avec la mise en place de blogs avec des moteurs divers et variés. Beaucoup moins en rédaction d'articles cela dit. Mais c'est hors sujet.

Ayant tout juste commencé un job de développeur en informatique, je n'avais pas plus le temps que la patience pour faire une liste d’exigences, mettre en place une solution dédiée et faire de la maintenance. Comme c'est souvent le cas dans ce genre de situation, il existait la solution rêvée: **Wordpress**.

Wordpress c'est simple, Wordpress c'est facile. Pas de maintenance, installation en 1 clique. Supporté et encouragé par pratiquement tout les hébergeurs. La voie royale. Je me suis dit : « Bon je trouve un bon hébergeur, je clique clique, mets un thème un peu sympa, fait une petite formation sur l'outil et c'est partis pour la postérité.» Je me suis gravement trompé.

<h4>1. Première version</h4>

Donc comme dit plus haut: Wordpress. Il y a trois ans, la solution dédiée la moins chère c'était de prendre un VPS OVH. Même avec un Wordpress dessus, ces petites machines virtuelles tenaient plutôt bien la charge. Et puis que veux le peuple pour 3,50 euros par mois. Cerise sur le gâteaux, il y avait une image Wordpress disponible au déploiement en un 1 clique. Il faut savoir que sur un hébergement dédie on a une machine physique vide et c'est au rôle de l'administrateur d'installer quelque chose dessus. Au contraire de ces solutions partagée de services déjà prêts.  
Super! Je clique… « Merci de bien attendre votre blog est en court de création. ». Super cool!  
Je me retrouve devant la console d'administration, je choisis un thème. Et hop, je vais voir ma mère pour lui montrer le bousin.

Oh purée. C'est la que je me suis rendu compte de ma première erreur. Wordpress c'est pas simple pour tout le monde.

<h5>1.1. les tâches du blogueur</h5>

Pour vous expliquer l'erreur mentionnée plus haut, le plus simple c'est de vous énumérer les tâches récurrentes qu'un blogueur doit répéter quotidiennement.

1. Écrire son texte
2. Faire relire son texte
3. Publier son texte
4. Modérer les nouveaux commentaires/spam
5. Tenir compte des nouveaux commentaires/mettre à jour un article existant

Oui mais tout ça c'est pour blogueur Sauf que le Wordpress il faut le faire vivre. Et donc on a les tâches d'administration:

1. Garder le blog opérationnel
2. Supprimer le spam
3. Mettre à jour le moteur

Et tout ça c'est si on a une personne unique, mais quand on a un utilisateur et un administrateur, ce dernier se tape aussi: Le Support (avec Majuscule car c'est tout et n'importe quoi la).

<h5>1.2. La chute de la première version</h5>

Pour être franc et raccourcir ce billet parmi toutes ces tâches ma mère ne sais en faire qu'une et encore partiellement : écrire son texte sur LibreOffice.  
<u>Et c'est normal.</u>
Il faut comprendre par la qu'elle ne fait pas partie de cette génération informatisée. L'ordinateur était facultatif lorsqu'elle travaillait.

Naturellement, je me tapais le reste (et plus encore). Mais comme je n'avais pas le temps c'était fait sommairement.

Au bout d'un moment, ma mère se retrouvait à demander quotidiennement de l'aide pour publier son dernier texte (comprendre par la prendre le document LibreOffice et le transformer en article sur Wordpress). Le blog quant a lui n'était plus maintenu faute de temps.

Et un jour Nginx le serveur web tomba. OK, bon je réinstalle. Nope ça retombe. OK, j'installe mais cette fois pas de clique clique -> j'y vais en mode hard. Je fais tout à la main. L'installation du serveur web, de l’interpréteur PHP, la mise en place du SSL, la mise en place du load-balancing, les règles de sécurité, tout! Nope ça retombe, l'export de la configuration est corrompue rien à faire et pas le temps de dépatouiller cette bouse.

***La première version était tombé. Elle était morte. Vive la seconde version.***

<h4>2. Leçons tirées</h4>

OK donc maintenant pour la conclusion, voici une énumérations des fausses idées reçues concernant la solution:

1. Wordpress n'est pas simple à utiliser (combien de fois j'ai du donner des explications pour publier, reformater, visualiser, modérer, etc…)
2. Wordpress n'est pas stable. Je suis un architecte système, c'est mon travail d'avoir un SLA parfait! Alors bien sûr avec un investissement relatif il y a moyen d'avoir un Wordpress super stable. Mais ça n'en vaut pas la chandelle. Il existe d'autre solutions.
3. La plupart des thèmes gratuits existant ne sont pas adaptés aux personnes âgées ou ayant des problèmes de vue (mauvaise taille de texte, mauvaise police de texte, mauvaise associations de couleurs, etc…)

Tout ce schmilblick s'est déroulé sur une période de deux ans. La version 2 (la version actuelle) corrige une grande partie des erreurs citées plus haut.
On a maintenant un système stable, simple à utiliser (ma mère n'a plus besoin que de LibreOffice et rien d'autre) et qui prends en compte l'ergonomie de lecture (faites attentions aux couleurs :) ).

Malheureusement, suite à la mise à jour du blog, j'ai changé le système de commentaire pour utiliser Disqus afin de justement de garder la partie modération des commentaire a un strict minimum et ce faisant ai perdu les commentaires existants. Je compte essayer de les récupérer si possible mais pour l'instant ce n'est pas possible.
