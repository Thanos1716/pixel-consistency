#version 150

#moj_import <fog.glsl>

uniform sampler2D Sampler0;

uniform vec4 ColorModulator;
uniform float FogStart;
uniform float FogEnd;
uniform float GlintAlpha;
uniform mat4 TextureMat;  // Added

// Pass the inverse of the TextureMat from the vertex shader to reduce the number of calculations.
in mat4 InverseTextureMat;  
in float vertexDistance;
in vec2 texCoord0;

out vec4 fragColor;

// Pixelate based on a scale, generally the size of the texture
vec2 pixelate(vec2 coords, vec2 scale) {
    return (floor(coords * scale) + 0.5) / scale;
}

// Transform and then pixelate a given fragment
vec2 transformPixelate(vec2 coords, mat4 matrix, vec2 scale) {
    return pixelate((matrix * vec4(coords, 0.0, 1.0)).xy, scale);
}

// This shader is used for most items in the GUI, in hand, and on the ground (excluding glass variants on the ground and trident in hand, possibly a few others)
void main() {
    // Original transform
    // vec4 color = texture(Sampler0, texCoord0) * ColorModulator;
    
    // Pixel consistent transform
    vec4 color = texture(Sampler0, (TextureMat * vec4((transformPixelate(texCoord0, InverseTextureMat, vec2(1024.0, 512.0))), 0.0, 1.0)).xy) * ColorModulator;
    if (color.a < 0.1) {
        discard;
    }
    float fade = linear_fog_fade(vertexDistance, FogStart, FogEnd) * GlintAlpha;
    fragColor = vec4(color.rgb * fade, color.a);
}
