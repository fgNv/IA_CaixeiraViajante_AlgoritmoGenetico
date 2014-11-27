app.factory("KnowledgeResource", function ($resource) {
    return $resource("/calculus", {}, {
        calculate: {
            method: "POST",
            isArray: false
        }
    });
});