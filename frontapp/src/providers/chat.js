export function createConnection(serverUrl) {
    return {
        connect() {
            console.log('✅ Connecting to ' + serverUrl + '...');

        },
        diconnect() {
            console.log('❌ Disconnected from ' + serverUrl);
        }
    };
}
