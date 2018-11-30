package ua.lviv.iot.rest;

import ua.lviv.iot.Good;
import ua.lviv.iot.persistence.dao.GoodDao;

import javax.enterprise.context.SessionScoped;
import javax.inject.Inject;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.io.Serializable;
import javax.ws.rs.core.Response;

@Path("/good")
@SessionScoped
public class Service implements Serializable {

    @Inject
    private GoodDao dao;

    @GET
    @Path("{id}/")
    @Produces(MediaType.APPLICATION_JSON)
    public Good getGood(final @PathParam("id") Integer id) {
        return dao.findById(id);
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response createGood(final Good good) {
        dao.persist(good);
        return Response.ok().build();
    }

    @DELETE
    @Path("/{id}")
    public Response deleteGood(@PathParam("id") Integer id) {
        dao.remove(id);
        return Response.status(200).entity("Good").build();
    }

    @PUT
    @Consumes(MediaType.APPLICATION_JSON)
    public Response replaceGood(Good good) {
        dao.persist(good);
        return Response.status(200).entity("Good").build();
    }

}
