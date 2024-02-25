/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.paths.fakeuploaddownloadfile.post;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.requestbody.GenericRequestBody;
import org.openapijsonschematools.client.requestbody.SerializedRequestBody;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.fakeuploaddownloadfile.post.requestbody.content.applicationoctetstream.ApplicationoctetstreamSchema;

import java.util.AbstractMap;
import java.util.Map;

public class RequestBody {
    public sealed interface SealedMediaType permits ApplicationoctetstreamMediaType {}

    public record ApplicationoctetstreamMediaType(ApplicationoctetstreamSchema.ApplicationoctetstreamSchema1 schema) implements SealedMediaType, MediaType<ApplicationoctetstreamSchema.ApplicationoctetstreamSchema1, Void> {
        public ApplicationoctetstreamMediaType() {
            this(ApplicationoctetstreamSchema.ApplicationoctetstreamSchema1.getInstance());
        }
        @Override
        public Void encoding() {
            return null;
        }
    }

    public static class RequestBody1 extends RequestBodySerializer<SealedRequestBody, SealedMediaType> {
        public RequestBody1() {
            super(
                Map.ofEntries(
                    new AbstractMap.SimpleEntry<>("application/octet-stream", new ApplicationoctetstreamMediaType())
                ),
                true
            );
        }

        public SerializedRequestBody serialize(SealedRequestBody requestBody) {
            ApplicationoctetstreamRequestBody requestBody0 = (ApplicationoctetstreamRequestBody) requestBody;
            return serialize(requestBody0.contentType(), requestBody0.body().getData());
        }
    }

    public sealed interface SealedRequestBody permits ApplicationoctetstreamRequestBody {}
    public record ApplicationoctetstreamRequestBody(ApplicationoctetstreamSchema.StringJsonSchema1Boxed body) implements SealedRequestBody, GenericRequestBody<ApplicationoctetstreamSchema.StringJsonSchema1Boxed> {
        @Override
        public String contentType() {
            return "application/octet-stream";
        }
    }
}
