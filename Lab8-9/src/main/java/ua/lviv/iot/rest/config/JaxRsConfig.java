package ua.lviv.iot.rest.config;

import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;

@ApplicationPath("resources")
public class JaxRsConfig extends Application {
    static {
        System.out.println("HERE IS OSTAPKO!!!");
    }
}