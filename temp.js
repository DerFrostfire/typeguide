var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
// Type with literals
var favoriteColor = 'red' | 'blue' | 'green' | 'yellow';
favoriteColor = 'blue';
//Generics
// < T > is used for example but we can use < X > or < A > etc.
var addId = function (obj) {
    var id = Math.floor(Math.random() * 1000);
    return __assign(__assign({}, obj), { id: id });
};
