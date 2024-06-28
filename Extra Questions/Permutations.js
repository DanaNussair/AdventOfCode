const permutations = (elements) => {
    if (elements.length === 0) return [[]];
    let firstEl = elements[0];
    let rest = elements.slice(1);

    let permsWithoutFirst = permutations(rest);
    let allPermutations = [];

    permsWithoutFirst?.forEach((perm) => {
        for (let i = 0; i <= perm.length; i++) {
            let permWithFirst = [
                ...perm.slice(0, i),
                firstEl,
                ...perm.slice(i),
            ];
            console.log(firstEl, "->", permWithFirst);
            allPermutations.push(permWithFirst);
        }
    });

    return allPermutations;
};

console.log(permutations(["a", "b", "c"]));
console.log(permutations(["b", "c"]));
console.log(permutations(["c"]));
