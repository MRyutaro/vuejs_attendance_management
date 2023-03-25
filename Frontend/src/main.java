@Path("/loginok")
@Produces(MediaType.APPLICATION_JSON)
public class LoginResource {
    @GET
    public Map<String, String> loginok() {
        return Map.of("message", "ログイン成功");
    }
}