package com.athlaes.test_api.web;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.context.annotation.Profile;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
@Profile(value = "!inMemory")
public class ApiController {

    @GetMapping(path = "/file/open")
    private String getFile() throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        JsonNode file = mapper.readTree(getClass().getResourceAsStream("/static/large-file.json"));
        return file.toPrettyString();
    }

    @GetMapping(path = "/hello")
    private String helloWorld() {
        return "Hello world";
    }
}
