/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    // return fibGenerator(n-1)+fibGenerator(n-2)
    a=0
    b=1
    while (true){
        yield a;
        [a,b]=[b,a+b]

    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */