# P11_Ameliorez_un_projet_existant_en_python
[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeH7711sJeOaZ_HOpwi3M7MjPOQeOPE2TyMxn-_NyxyHu_O2tm&s)](https://openclassrooms.com/fr)  
![(http://206.189.30.229/substitute/home/)](Readme/biscuits.png)  
![(http://206.189.30.229/substitute/home/)](Readme/it_logo.png)  

# But du projet


    Bonjour,

    Je vous remercie pour le travail réalisé.
    Néanmoins nous avons découvert qu’il manquait une fonctionnalité importante que nous aimerions développer.
    Combien de temps cela vous prendrait-il ?

    Nous avons également remarqué des dysfonctionnements (rien n’apparaît lorsque nous lançons Internet Explorer).
    Nos développeurs ont essayé de résoudre les bugs mais en vain, apparemment.
    Ils viennent de me dire de vous contacter car les tests sont cassés (je ne sais pas ce que cela signifie mais je transmets)
    et menacent la production (ça, j'ai bien compris - ils ont travaillé directement sur le site en ligne !).

    C’est tout pour aujourd’hui.

    Merci.

    Cordialement,

    Dona Jimena

# Contexte du projet
La plateforme PurBeurre a été sélectionné en tant que base du projet.  
Rappel : Voici [le cahier des charges](/Readme/Cahier_des_charges.pdf) sur lequel s'appuie la plateforme PurBeurre.  

# Organisation du projet
Ce projet est réalisé selon une méthodologie agile.  
Sa planification est disponible via ce [Trello](https://trello.com/invite/b/SYTimIfb/142082c5c7aaaf9c6b1b187ef790e314/p11ameliorezunprojetexistantavecpython).  

# Version du projet
Plateforme web - PurBeurre : 1.2

    - Langage de programmation : Python 3.8
    - Framework : Django 3.1.2
    - Serveur d'application : Gunicorn 20.0.4
    - Serveur web : Nginx 1.18.0
    - Base de données : Postgresql 13
    - Hébergeur : Digital Ocean

# Intégration Continue  
A chaque modification du projet, ajout de nouvelles fonctionnalités ou de corrections,  
le projet est envoyé sur la branche [1.2_stagging](https://github.com/StephenAOGOLO/P10_Deployez_votre_application_sur_un_serveur/tree/1.2_staging). C'est à ce niveau que le service Travis entre en fonction.  
Ce service cree un environnement éphémère de production, proche de l'environnement du serveur hébergé.  
Il exécute deux campagnes de tests. Une campagne de tests unitaires/fonctionnels et une campagne de tests d'intégration.
Les tests unitaires utilisent les modules Django "TestCase" et "SimpleTestCase".  
Les tests d'intégration sont gérés par le module selenium couplé à un WebDriver.  
Ces derniers sont testés sur le navigateur Chrome.  


# Auteur
Stephen A.OGOLO

# Remerciements
Merci pour cette lecture et pour l'attention portée à ces informations.  
Bonne utilisation !
