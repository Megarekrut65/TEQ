import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";
import { getToken } from "@/js/utility/token.js";

export const poolGetApi = () => {
    const request = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
    };
    return sendAsync(API + `pool/`, request);
};

export const categoryCreateApi = ({ name }) => {
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
        body: JSON.stringify({ name }),
    };

    return sendAsync(API + "category/", request);
};

export const categoryGetApi = (categoryId) => {
    const request = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
    };
    return sendAsync(API + `category/${categoryId}/`, request);
};

export const categoryDeleteApi = (categoryId) => {
    const request = {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
    };
    return sendAsync(API + `category/${categoryId}/`, request);
};

export const categoryUpdateApi = (categoryId, { name }) => {
    const request = {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
        body: JSON.stringify({ name }),
    };

    return sendAsync(API + `category/${categoryId}/`, request);
};

export const itemCreateApi = (
    categoryId,
    { text, type, choices, grade, allowProportion, correctAnswer = null, minSimilarPercent = 0 },
) => {
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
        body: JSON.stringify({
            text,
            type,
            choices,
            correctAnswer,
            grade,
            allowProportion,
            minSimilarPercent,
        }),
    };

    return sendAsync(API + `category/${categoryId}/item/`, request);
};

export const itemDeleteApi = (categoryId, index) => {
    const request = {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
    };
    return sendAsync(API + `category/${categoryId}/item/${index}`, request);
};

export const itemUpdateApi = (
    categoryId,
    index,
    { text, type, choices, grade, allowProportion, correctAnswer = null, minSimilarPercent = 0 },
) => {
    const request = {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
        body: JSON.stringify({
            text,
            type,
            choices,
            correctAnswer,
            grade,
            allowProportion,
            minSimilarPercent,
        }),
    };

    return sendAsync(API + `category/${categoryId}/item/${index}`, request);
};
