
Hello, my name's donal
Software testing - absolutely no-ones favourite topic. Actually, it is mine.
I have a friend who is a tester who keeps asking me 'so you want to be a developer...'
No! Don't say that to a 'tester' 'like me', it is potentially offensive!

THANKS!
Thanks for the organisers
Thanks to bloomberg
Thanks to the python community

WHAT'S THE TALK ABOUT?
    - Make an apology. Description of this topic has changed! A lot!
    - Originally going to speak about hypothesis and acceptance testing and robot.
    - But, when I was writing, I found I needed to explain some of the basics before I could talk about the complex stuff. That's a beginner mistake for you!

I LOOKED AT STACK LAST WEEK
    - No of jobs that mention 'python' == (205)
    - No of jobs that mention 'python' AND 'test' (100) == (49%)
    - No of jobs where job role is 'Test Developer/QA' == 134
    - No of jobs where job role is 'Test Developer/QA' AND mention 'python' == 38 (28%)

TESTING IS NOT A POPULAR TOPIC
    - painful
    - unpopular
    - ideally, we won't have to test
    - we learn to develop...then we learn to test
    - I've even heard someone say "if they write a bug they make them wear a dunce hat"

BUT IS THERE A DIFFERENCE BETWEEN TESTING AND DEVELOPMENT?
    - that's a question I am asking you. I'm not going to tell you my opinion.
    - but testing has a lower priority in most teams because we sell features not tests.
    - i.e. test is a cost, features are an area of profit.
    - bugs are a lot like radioactivity
    - and radioactivity is potentially a source of death and a source a power. hiroshama/nuclear fusion....

BUT WHY DO PEOPLE WRITE TESTS?
    1) Because we something goes wrong, they can point to the tests to show that they are trying not to release buggy products.
    2) To find out the product requirements (tdd).
    3) Help provide team with confidence that they can release the product.
    4) To catch bugs.

TIP 1: DON'T CALL IT AUTOMATED TESTING
    - Auto means 'free' or free from human involvement
    - No such thing.
    - Programmatic testing....

RULE 1: KEEPING IT SIMPLE IS THE AIM OF THE TESTING GAME
    - If the adopted testing method increases the complexity of the project, you are doing it wrong.
    - Tests needs to handle complexity by breaking down the domain into manageable parts.

RULE 0: TESTING IS NOT VERIFICATION
    - This is the foundation to understand. 
    - 'Testing' will not prove the product is free from bugs. Only verification can do this.
    - Significant systems, testing alone is irresponsbile.
    - Quickly continue.

TIP 2: CHOOSE YOUR TOOL: THE SINGLE AFTERNOON SUGGESTION
    - Cause tIP 1 was DON'T CALL IT AUTOMATED TESTING
    - testing is all about appopriate tool choice
    - Don't adopt tools that take longer than an afternoon to understand
    - See bottle: https://bottlepy.org/docs/dev
        - Better than cherrypy
    - See expects: https://github.com/jaimegildesagredo/expects
    - pytest (fixtures, anyone?)
    - robot framework

PYTHON EXCEPTION: WAIT PYTHON TAKES MORE THAN AN AFTERNOON TO LEARN
    (raise an assertion exception, python takes longer than one afternoon )
    BUT YOU SAID...

    - RULE 1: KEEPING IT SIMPLE IS THE AIM OF THE TESTING GAME
    - TIP 2: CHOOSE YOUR TOOL: THE SINGLE AFTERNOON SUGGESTION

    - Yes. I wholly advocate that testers using python come to wholly understand how to use it.
    - But that's the exception that facilitates the rule.
    - Knowing python empowers you as a tester to write you own frameworks in an afternoon.
    - Better than using someone else's better but more complex thing because of the complexity burden other tools will impose upon your time.
    - TESTING time is TIGHT. No time for new frameworks!
    - Ducking typing and interpretation means power/flexibility and GOD AWFUL CODE!
    - Walks like a duck, quack like a duck, is as ugly as d-ck
    - Good tester but bad python programmer? [...right.....]

SHOW ME THE CODE!
    - Enough talking, more walking walking donal.
    - OK, replace your test framework. You don't need it.



