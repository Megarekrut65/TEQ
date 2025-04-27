import { loginApi, registerApi } from "@/js/api/user.js";
import { getToken } from "@/js/utility/token.js";
import i18n from "@/i18n/index.js";

const userKey = "user";

const saveUser = (user) => {
    localStorage.setItem(userKey, JSON.stringify(user));
};

export const getUser = () => {
    const data = localStorage.getItem(userKey);
    if (!data) return null;

    try {
        const user = JSON.parse(data);
        if (!("token" in user)) return null;

        return user;
    } catch (error) {
        console.log(error);

        return null;
    }
};

export const login = ({ email, password }) => {
    return loginApi({ email, password }).then((user) => {
        saveUser(user);
        window.dispatchEvent(new CustomEvent("auth", { detail: user }));
        return user;
    });
};

export const register = ({ fullname, email, password }) => {
    return registerApi({ fullname, email, password }).then((user) => {
        saveUser(user);
        window.dispatchEvent(new CustomEvent("auth", { detail: user }));
        return user;
    });
};

export const ifAuthenticated = (to, from, next) => {
    const token = getToken();

    if (token) {
        next();
        return;
    }

    next({ name: "auth", params: { locale: i18n.getLocale() } });
};

export const logout = () => {
    localStorage.clear();
    window.dispatchEvent(new CustomEvent("auth", { detail: null }));
};
