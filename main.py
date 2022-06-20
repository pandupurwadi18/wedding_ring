### Project Wedding Ring game
### Pandu Purwadi

print('''
                 ,    ,    .
             , ~@  `@ @~  `@  ,
           ~@ @ZXZ%%X&ZX%Z%XZ@`,
        ;@ %  @.~@,-.&&,-.@~ @ @H @~
        ,@X  ~  @(   )(   )@"  ~@X
        H  @     )   ()   (      ;@H@. ,
    `@X ,   `   '-=o=-'=o=-'         %@
 `@ %  @                            ,@ X@~
 ~ X@   "                            "  %  ,
;@H                      ,-.             H@.
  %@~            .,.    (/)_)          `@X
  H `          ,*@@@*.  d " b          ,@%@~
  %@~           &&&-b    \ /           ~@%
  X@.           && /: ,-/[x]\-.        ' X@
~@H              &!! /  \|M|/  \         H `
 'X@           /](  )[\ /|M|\~| |        X@:
  H           | ( ~~ ) !\| |/ | |      `@%
  H@.         `='8  [`=' |-|  | |      ~ H
,@X            \\(@*)//  |-|  |/         H@~
  %@~         / (*@@*) \_| |__|        `@X
  H `        /   (*@)   \ |  |         ,@%@~
  X@        /  ,~ ;: ~`  \|  |           H
`@% '      /     :  ;     \  |         ~@% ,
  H       /~       ;       \ |           X@.
  X@.    /.,   ~@~    ~@~   \|           H
  H      /  '"*.,,*"'*,.,*'"\|         `@H
 @X@~   /                    \          X@
~ %@,  /                      \        ,@H ~
  H   /                        \         H
  H@.@~                       ~@\        %@,
,@X `'"*'*,  ~@~     ~@~  ,.*'"*"      ~@X
  H@~      '"*,.*"'"*.,*"'               H@.
  H><>gpyy<><><><><><><><><><><><><><><>
''')
print("Welcome to Wedding Ring! \nYour mission is to find right ring")
choice_1 = input('You\' re heading to ring shop, what do you want to buy? Type "diamond" or "stone".\n').lower()

if choice_1 == "diamond":
    choice_2 = input('You\'ve bought diamond ring. There is a beautiful girl beside you. Type "give" or "run".\n').lower()
    if choice_2 == "run":
        choice_3 = input('Finally, please choice between three color, "red", "yellow", or "green".\n')
        if choice_3 == "red":
            print("Congrats! You win")
        elif choice_3 == "yellow":
            print("Wrong girl, Game over")
        elif choice_3 == "green" :
            print("bad luck, Game over")
        else:
            print("Your answer not relevant. Game over")
    else:
        print("You're unfaithful. Game over")
else :
    print("Bad decision for your partner. Game over")