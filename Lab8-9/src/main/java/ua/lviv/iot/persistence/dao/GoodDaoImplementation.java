package ua.lviv.iot.persistence.dao;

import ua.lviv.iot.Good;

import javax.annotation.Resource;
import javax.persistence.EntityManager;
import javax.transaction.UserTransaction;
import java.io.Serializable;

public class GoodDaoImplementation extends  AbstractDao<Good> implements GoodDao, Serializable {
    private EntityManager entityManager;

    @Override
    protected Class<Good> getEntityClass() {
        return Good.class;
    }

    @Resource
    private UserTransaction userTransaction;
}
