import { API } from "./api";
import { partnersRoutes, pricingRoutes, servicesRoutes, socialRoutes } from "./routes";

export const pricingData = () => API.get({
    url: pricingRoutes,
    headers: {
        'Content-Type': 'application/json'
    }
})

export const partnersData = () => API.get({
    url: partnersRoutes,
    headers: {
        'Content-Type': 'application/json'
    }
})

export const socialData = () => API.get({
    url: socialRoutes,
    headers: {
        'Content-Type': 'application/json'
    }
})

export const servicesData = () => API.get({
    url: servicesRoutes,
    headers: {
        'Content-Type': 'application/json'
    }
})