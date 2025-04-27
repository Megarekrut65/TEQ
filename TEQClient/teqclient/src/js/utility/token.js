export const getToken = () => {
    const jsonUser = localStorage.getItem("user");
    if (!jsonUser) return null;

    const user = JSON.parse(jsonUser);
    if (!user) return null;

    if ("token" in user) return user.token;
    return null;
};
