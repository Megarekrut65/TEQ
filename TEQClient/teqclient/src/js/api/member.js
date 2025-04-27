import { sendAsync } from "@/js/utility/request.js";
import { API } from "@/js/api/api.js";
import { getToken } from "@/js/utility/token.js";

export const memberCreateApi = (testId, { emails }) => {
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
        body: JSON.stringify({ emails }),
    };
    return sendAsync(API + `member/${testId}/add`, request);
};

export const memberListApi = (testId) => {
    const request = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
    };
    return sendAsync(API + `members/${testId}`, request);
};

export const memberDeleteApi = (memberId) => {
    const request = {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${getToken()}`,
        },
    };
    return sendAsync(API + `member/${memberId}`, request);
};
