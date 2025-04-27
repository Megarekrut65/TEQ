import { reactive } from "vue";

const getAlertBus = () => {
    return reactive({
        alerts: [],

        addAlert(msg, alert = "info", timeout = 10) {
            const obj = { msg: msg, alert: alert };
            this.alerts.push(obj);
            if (timeout > 0) {
                setTimeout(() => this.closeAlert(obj), timeout * 1000);
            }
        },
        closeAlert(alert) {
            this.alerts.splice(this.alerts.indexOf(alert), 1);
        },
    });
};

export const alertBus = getAlertBus();
