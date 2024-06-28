const combinations = (elements) => {
    if (elements.length === 0) return [[]];
    let firstEl = elements[0];
    let rest = elements.slice(1);

    let combsWithoutFirst = combinations(rest);
    let combsWithFirst = [];

    combsWithoutFirst?.forEach((comb) => {
        let newCombsWithFirst = [...comb, firstEl];

        combsWithFirst.push(newCombsWithFirst);
    });

    return [...combsWithoutFirst, ...combsWithFirst];
};
