package org.openapijsonschematools.client.paths.fake.post.security;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.securityrequirementobjects.SecurityRequirementObject;
import org.openapijsonschematools.client.securityschemes.SecurityScheme;
import org.openapijsonschematools.client.components.securityschemes.HttpBasicTest;

import java.util.List;
import java.util.Map;
import java.util.AbstractMap;

public class FakePostSecurityRequirementObject0 extends SecurityRequirementObject {

    public FakePostSecurityRequirementObject0(
        HttpBasicTest securityScheme0
    ) {
        super(
            Map.ofEntries(
                new AbstractMap.SimpleEntry<SecurityScheme, List<String>>(
                    securityScheme0,
                    List.of()
                )
            )
        );
    }
}
