# Conception logicielle

[![Vérifications contre reader-ergonomics](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/checks.yml/badge.svg?branch=master)](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/checks.yml?query=branch%3Amaster)
[![Site](https://github.com/Tewf/reader-ergonomics-software-design/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-software-design/)

Comment écrire les documents qui conçoivent un logiciel avant le code : spécifications d'algorithme, documents de
conception, registres de décisions, descriptions d'architecture et schémas de système. Chacun est écrit au moindre
coût pour son lecteur, et pour celui qui l'implémente, une personne ou un modèle. Cinq formes donnent à chaque document son squelette, et
des vérifications trouvent un document par sa ligne Shape, si bien qu'elles tournent en CI.

Trois revues lisent aussi les preuves sur la conception elle-même. La conception d'algorithmes nourrit deux principes
et la spécification d'algorithme, la conception de systèmes un principe. La conception d'architecture est une revue
dont aucune règle n'est encore tirée.

Il étend [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). Les principes généraux, leurs niveaux de
preuve et les vérifications y vivent et ne sont pas répétés ici. Ce dépôt n'ajoute que ce qui est propre à la
conception logicielle et à son écriture : ses preuves, ses principes et les formes de ses documents.

Commencer par la [fiche](standard.md), en anglais. [In English](README.md).

## Utilisation

Dix minutes, sans lire les revues. La forme générale de la famille est le
[Take your own version](https://github.com/Tewf/reader-ergonomics/blob/bfbe9f7ed27bfdca0c6a4922d0b3e302f9e55d3f/README.md#take-your-own-version) de reader-ergonomics ; voici ce qu'elle donne pour la conception logicielle :

1. **Épingler le standard par commit**, pour que ses vérifications ne changent pas sous vos pieds :
   `git clone https://github.com/Tewf/reader-ergonomics && git -C reader-ergonomics checkout bfbe9f7` (v1.18.2).
2. **Copier ce qu'il faut, une fois.** Le squelette d'une [forme](shapes/README.md), avec sa ligne `**Shape:**`, et
   [`checks/local/`](checks/local/) dans le `checks/local/` de son dépôt. Les copies sont à vous : un changement
   ultérieur ici ne touche rien de ce que vous avez copié. Notez le commit d'où vous copiez, pour comparer plus tard.
3. **Configurer** avec un `checks/config.toml` :

   ```toml
   extends = "reader-ergonomics"

   [readable_measure]
   stylesheets = []   # pas de feuille de style de site à mesurer

   [sufficient_contrast]
   stylesheets = []
   ```

4. **Remplir et vérifier.** Ranger les documents dans un dossier nommé d'après ce qu'ils servent, comme `design/`, et
   lancer `python3 reader-ergonomics/checks/run.py .`, en CI aussi. Un document est vérifié contre la forme que lie sa
   ligne Shape, et chaque schéma Mermaid contre les règles des schémas. Un [exemple](examples/README.md) rempli de
   chaque forme passe ; on peut partir de l'un d'eux.
5. **Contester** en ouvrant une issue sur ce dépôt, avec les preuves ; une règle du standard lui-même va dans les
   issues de reader-ergonomics.

| Vérification | Vérifie | Échoue quand |
|---|---|---|
| `algorithm-specs` | les spécifications d'algorithme | une partie manque, le contrat vient après les étapes, les étapes sont en prose, ou les exemples ne sont pas un tableau |
| `design-docs` | les documents de conception | la décision demandée ne vient pas en premier, une partie requise ou le tableau des alternatives manque |
| `diagram-keys` | chaque schéma Mermaid | un schéma n'a pas de légende, ou une flèche de flowchart pas d'étiquette |
| `decision-records`, dans reader-ergonomics | les registres de `decisions/` | un registre enfreint l'une des quatre règles de la forme |

> **État :** version 1.0.0, publiée le 2026-10-29. Sept revues de littérature sont écrites dans [evidence/](evidence/), chacune une revue
> multivocale de la recherche et de la pratique ; leurs chiffres ont été vérifiés contre les sources primaires (quatre
> le 2026-10-28, trois le 2026-10-29). Les cinq formes sont écrites (spécification d'algorithme, document de
> conception, registre de décision, description d'architecture, schéma de système), ainsi que huit principes et la
> [fiche](standard.md). C'est une lecture informelle de la recherche et de la pratique publiées : pas une norme
> officielle, pas une étude évaluée par des pairs, pas un résultat nouveau, et pas une revendication de l'état de l'art.
>
> **Comment il est fait :** avec Claude, un assistant IA d'Anthropic, sous la direction du mainteneur, comme
> reader-ergonomics. Des agents IA rédigent les revues de littérature ; chaque référence est résolue par script, et un
> chiffre lu seulement dans un résumé est marqué « (secondary) ». Les corrections sont bienvenues sous forme d'issues.

## Périmètre

| | Quoi | Pourquoi |
|---|---|---|
| dedans | les documents sur un système : descriptions d'architecture, registres de décisions, documents de conception, pseudo-code, schémas de composants et de flux de données | le lecteur est l'objet, comme dans reader-ergonomics |
| dedans | la conception du système au niveau abstrait, avant le code : conception d'architecture, conception de système, conception et spécification d'algorithmes | la conception est ce à partir de quoi un implémenteur, une personne ou un modèle, travaille |
| dehors | les langages de programmation et leur implémentation | un autre objet, avec ses propres preuves et ses propres vérifications |
| dehors | l'organisation du code en fichiers et en dossiers | déjà couverte par les principes de collection de reader-ergonomics |

## Organisation

La même que reader-ergonomics, pour qu'un lecteur de l'un s'oriente dans l'autre :

- `evidence/<sujet>/` : une revue de littérature par sujet, un fichier par étape (cadre, revue, état de l'art,
  positionnement, arguments contre, référence de comparaison), plus son protocole et ses sources notées ; sept sujets ;
- [`shapes/`](shapes/) : le squelette de chaque type de document, avec les preuves derrière chaque partie. Sont
  écrites la [spécification d'algorithme](shapes/algorithm-specification.md), le
  [document de conception](shapes/design-document.md), le [registre de décision](shapes/decision-record.md), la
  [description d'architecture](shapes/architecture-description.md) et le [schéma de système](shapes/system-diagram.md) ;
- [`examples/`](examples/README.md) : un document rempli de chaque forme, vérifié en CI comme un autre ;
- [`decisions/`](decisions/) : les registres des choix de conception de ce dépôt ;
- [`principles/`](principles/README.md) : seulement là où la conception logicielle diffère du standard général, huit
  principes en trois groupes (spécification, décision, structure), réunis sur la [fiche](standard.md) ;
- [`reader-styles/`](reader-styles/README.md) : les lecteurs propres à ce genre, un modèle qui implémente et un nouveau
  venu ;
- [`AGENTS.md`](AGENTS.md) et [`llms.txt`](llms.txt) : comment modifier ce dépôt, et son index pour les modèles de
  langage ;
- `checks/` : les réglages qui étendent ceux de reader-ergonomics, et les vérifications locales avec leurs tests.

## Vérifier

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py chemin/vers/ce/depot
```

L'intégration continue lance les mêmes vérifications à chaque push, et échoue à la moindre erreur
([checks.yml](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/.github/workflows/checks.yml)). Le
badge en haut en donne le dernier résultat : la preuve que ce dépôt respecte le standard qu'il étend. Chaque push sur
master construit aussi le site, [tewf.github.io/reader-ergonomics-software-design](https://tewf.github.io/reader-ergonomics-software-design/)
([pages.yml](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/.github/workflows/pages.yml)).

## Licence

Le code sous [Apache License 2.0](LICENSE) ; la prose sous [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Réutilisez-le comme
vous voulez, en citant ce dépôt ; [CITATION.cff](CITATION.cff) donne une citation si besoin.
